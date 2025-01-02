def ImageToText(imagepath, googleapikey):
  import os
  import google.generativeai as genai
  from dotenv import load_dotenv

  load_dotenv()
  genai.configure(api_key=os.getenv(googleapikey))

  def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini.

    See https://ai.google.dev/gemini-api/docs/prompting_with_media
    """
    file = genai.upload_file(path, mime_type=mime_type)
    # print(f"Uploaded file '{file.display_name}' as: {file.uri}")
    return file

  # Create the model
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
  )

  # TODO Make these files available on the local file system
  # You may need to update the file paths
  files = [
    upload_to_gemini(f{imagepath}, mime_type="image/png"),
  ]

  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          files[0],
          "extract information from image",
        ],
      },
      # {
      #   "role": "model",
      #   "parts": [
      #     "LAP3NV",
      #   ],
      # },
    ]
  )

  response = chat_session.send_message("t")
  return response
  # print("test",response.text)