import json
import logging
import uvicorn
from fastapi import FastAPI, Response


# log
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(name)-9s][%(levelname)-5s] %(message)s (%(filename)s:%(lineno)d)",
    datefmt="%Y-%m-%d %H:%M:%S"
    )
main_logger = logging.getLogger("main")
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True
uvicorn_error = logging.getLogger("uvicorn.error")
uvicorn_error.disabled = True

# create app
app = FastAPI(
    title = "report preprocessing",
    desciption = "report preprocessing",
    version = "version 1.0.0",
    redoc_url = None
)

@app.get("/get_report_object")
async def get_report_object():
    return Response(json.dumps({"data": "success"}),
                    status_code=200, media_type='application/json')


@app.on_event("startup")
async def startup_event():
    """fastapi startup"""
    main_logger.info("startup!!")


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        )
