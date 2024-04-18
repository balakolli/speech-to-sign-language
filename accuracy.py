import os
def calculate_accuracy(output_folder, isl_folder):
    output_videos = os.listdir(output_folder)
    isl_videos = os.listdir(isl_folder)

    total_videos = len(output_videos)
    correct_matches = 0

    for output_video in output_videos:
        if output_video in isl_videos:
            correct_matches += 1

    accuracy = (correct_matches / total_videos) * 100
    return accuracy

# Example usage
output_folder = "output_videos"
isl_folder = "ISL_Gifs"

accuracy = calculate_accuracy(output_folder, isl_folder)
print("Accuracy:", accuracy, "%")