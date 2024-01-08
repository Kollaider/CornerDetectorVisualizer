import pandas as pd
import requests
from model import PlotDrawer


def download_json(url: str, save_path: str) -> None:
    """
    Download JSON data from the given URL and save it to the specified path.

    Parameters:
    - url (str): URL of the JSON file.
    - save_path (str): Path to save the downloaded JSON file.
    """
    response = requests.get(url)
    with open(save_path, "wb") as f:
        f.write(response.content)

def main() -> None:
    """
    Main function to execute the data download, analysis, and plot creation.
    """
    url = "https://ai-process-sandy.s3.eu-west-1.amazonaws.com/purge/deviation.json"
    json_file_path = "deviation.json"

    download_json(url, json_file_path)
    df = pd.read_json(json_file_path)
    drawer = PlotDrawer()

    figure = drawer.draw_plots(df)
    drawer.save_plot(figure, "plots", "ground_truth_vs_model.png")

if __name__ == "__main__":
    main()