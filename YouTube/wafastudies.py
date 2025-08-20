from pytube import Playlist
import os

def download_playlist(url, output_path=None):
    """
    Downloads all videos from a given YouTube playlist URL.

    Args:
        url (str): The URL of the YouTube playlist.
        output_path (str, optional): The directory where videos will be saved.
                                     Defaults to a folder named after the playlist title.
    """
    try:
        # Create a Playlist object from the URL
        playlist = Playlist(url)

        # Print the title of the playlist to confirm it's working
        print(f"Downloading playlist: {playlist.title}")
        print(f"Number of videos: {len(playlist.video_urls)}")

        # If no output path is specified, create a folder with the playlist's title
        if output_path is None:
            output_path = f'./{playlist.title}'

        # Create the directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Created directory: {output_path}")

        # Loop through each video URL in the playlist
        for video_url in playlist.video_urls:
            try:
                # Get the YouTube object for the current video
                yt = playlist.video_for_url(video_url)

                # Get the highest resolution stream with both video and audio
                # This is a good general-purpose option for quality.
                # If you want to download only audio, use:
                # stream = yt.streams.filter(only_audio=True).first()
                stream = yt.streams.get_highest_resolution()
                
                if stream is None:
                    print(f"Skipping '{yt.title}' - no progressive stream found.")
                    continue

                print(f"Downloading: {yt.title}...")

                # Download the video to the specified output path
                stream.download(output_path)

                print(f"Downloaded '{yt.title}' successfully!")

            except Exception as e:
                print(f"Error downloading video: {video_url}")
                print(f"An error occurred: {e}")
                continue # Continue to the next video even if one fails

        print("\nPlaylist download complete!")

    except Exception as e:
        print(f"Error: An issue occurred with the playlist URL or pytube.")
        print(f"Please check the URL and your internet connection.")
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage:
    # Replace the URL below with the URL of the playlist you want to download.
    'https://www.youtube.com/watch?v=Mc9JAra8WZU&list=PLMWaZteqtEaLTJffbbBzVOv9C0otal1FO' = input("Enter the YouTube playlist URL: ")
    download_playlist(playlist_url)