import matplotlib.pyplot as plt
from io import BytesIO
import base64


def generate_histogram_html(frequency_data):
    # Create the histogram chart
    plt.bar(frequency_data.keys(), frequency_data.values(), color="skyblue")
    plt.xlabel("Growth Time")
    plt.ylabel("Frequency")
    plt.title("Berry Growth Time Histogram")

    # Save the graph as an image in memory
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)

    image_base64 = base64.b64encode(buffer.read()).decode()

    # Generate the HTML that includes the image
    html_content = f"""
    <html>
        <body>
            <h1>Berry Growth Time Histogram</h1>
            <img src='data:image/png;base64,{image_base64}' />
        </body>
    </html>
    """
    return html_content
