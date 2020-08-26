from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
image_urls_map = {
    "https://assets.smallcase.com/images/smallcases/200/SCSB_0003.png": "https://smallcase.zerodha.com/smallcase/SCSB_0003",
    "https://assets.smallcase.com/images/smallcases/200/SCSB_0004.png": "https://smallcase.zerodha.com/smallcase/SCSB_0004",
    "https://assets.smallcase.com/images/smallcases/200/SCET_0005.png": "https://smallcase.zerodha.com/smallcase/SCET_0005",
    "https://assets.smallcase.com/images/smallcases/200/SCNM_0007.png": "https://smallcase.zerodha.com/smallcase/SCNM_0007",
    "https://assets.smallcase.com/images/smallcases/200/SCAW_0001.png": "https://smallcase.zerodha.com/smallcase/SCAW_0001",
}


@app.route("/")
def index():
    key = random.choice(list(image_urls_map))
    return render_template("index.html", smallcase_url=image_urls_map, image_url=key)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
