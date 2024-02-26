import config  # pylint: disable=unused-import

import uvicorn
from fastapi import FastAPI
import secure

app = FastAPI()

server = secure.Server().set("Secure")

csp_config = config.FastAPIExampleConfig.get().csp_config
if csp_config.configure_csp:
    print("Got here")
    csp = (
        secure.ContentSecurityPolicy()
        .default_src(*csp_config.default_src)
        .base_uri(*csp_config.base_uri)
        .connect_src(*csp_config.connect_src)
        .frame_src(*csp_config.frame_src)
        .img_src(*csp_config.img_src)
    )
else:
    csp = secure.ContentSecurityPolicy()

hsts = secure.StrictTransportSecurity().include_subdomains().preload().max_age(2592000)

referrer = secure.ReferrerPolicy().no_referrer()

permissions_value = (
    secure.PermissionsPolicy().geolocation("self", "'spam.com'").vibrate()
)

cache_value = secure.CacheControl().must_revalidate()

secure_headers = secure.Secure(
    server=server,
    csp=csp,
    hsts=hsts,
    referrer=referrer,
    permissions=permissions_value,
    cache=cache_value,
)


@app.middleware("http")
async def set_secure_headers(request, call_next):
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


@app.get("/")
async def root():
    return {"message": "Secure"}


if __name__ == "__main__":
    uvicorn.run(app, port=8081, host="localhost")
