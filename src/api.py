import sys
import os
import uvicorn
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.post("/hello", tags=["hello"])
async def api_say_hello(name:str=None):

  if not name:
    greeting = "Please enter a name for personalized greeting"
  else:
    greeting = f"Hello {name}, have a nice day!"
  
  res = {
    "message": greeting
  }

  return res

@app.post("/api/upload", tags=["input"])
async def api_files_upload(file: UploadFile):

  data_path = "../data"

  os.makedirs(data_path, exist_ok=True)

  tgt_path = os.path.join(data_path, file.filename)
  with open(tgt_path, 'wb') as fl:
    fl.write(file.file.read())

  res = {
    "uploaded": file.filename
  }

  return res

if __name__ == "__main__":
  if "dev".lower() in sys.argv:
    print("Dev Mode")
    uvicorn.run(app="__main__:app", host="0.0.0.0", port=8000, debug=True, reload=True)
  else:
    print("Prod Mode")
    # import webbrowser
    # webbrowser.open("http://localhost:%s" %conf_settings.API_PORT)
    uvicorn.run(app="__main__:app", host="0.0.0.0", port=8000)