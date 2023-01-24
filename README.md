# lambdaauthorization


En este ejemplo, utilizamos FastAPI para definir dos endpoints /admin y /user y utilizamos Magnum para validar el token de acceso enviado en la solicitud. Se crea un decorador llamado role_validation que recibe una lista de roles permitidos y devuelve otro decorador que se encarga de validar si el token enviado en la solicitud tiene el rol adecuado. Si el usuario tiene el rol adecuado, se devuelve un mensaje de acceso permitido. Si no, se devuelve un error HTTP 401 (No autorizado).

Ten en cuenta que en este ejemplo debes reemplazar los valores "your_client_id", "your_client_secret" y "your_tenant_id" con los valores correspondientes a tu aplicación de Azure AD. Ademas se deben instalar las librerias "fastapi" y "magnum" antes de poder utilizarlas en tu código.