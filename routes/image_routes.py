from flask import Blueprint, request, jsonify
from detection import run_prediction
from report import send_report
import threading

image_bp = Blueprint("image_bp", __name__)

@image_bp.route("/detect", methods=["POST"])
def detect_defects():
    if "file" not in request.files:
        return jsonify({"error" : "файл не передан в запросе"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error":"Не указан файл"}), 400

    image_bytes = file.read()

    detection_res = run_prediction(image_bytes)

    if detection_res["defect_detected"]:
        threading.Thread(target=send_report, args=(detection_res, file.filename))

    return jsonify(detection_res)
