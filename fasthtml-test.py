from fasthtml.common import *
from pathlib import Path
app, rt = fast_app()
upload_dir = Path("filez")
upload_dir.mkdir(exist_ok=True)
@rt('/')
def get():
    return Titled("多文件上传演示",
        Article(
            Form(hx_post=upload_many, hx_target="#result-many")(
                Input(type="file", name="files", multiple=True),
                Button("上传", type="submit", cls='secondary'),
            ),
            Div(id="result-many")
        )
    )
def FileMetaDataCard(file):
    return Article(
        Header(H3(file.filename)),
        Ul(
            Li('大小: ', file.size),
            Li('内容类型: ', file.content_type),
            Li('头部信息: ', file.headers),
        )
    )
@rt
async def upload_many(files: list[UploadFile]):
    cards = []
    for file in files:
        cards.append(FileMetaDataCard(file))
        filebuffer = await file.read()
        (upload_dir / file.filename).write_bytes(filebuffer)
    return cards
serve()