

from playwright.sync_api import Playwright


class APIUtils:
    def createToken(self,playwight:Playwright,user_credentials):
        user_email = user_credentials["username"]
        user_password = user_credentials["password"]
        api = playwight.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api.post("/api/ecom/auth/login",data={"userEmail":user_email,"userPassword":user_password})
        assert response.ok
        print(response.json())
        return response.json()["token"]

    def createOrder(self,playwight:Playwright,user_credentials):
        api = playwight.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api.post("/api/ecom/order/create-order",data={"orders":[{"country":"India","productOrderedId":"68a961459320a140fe1ca57a"}]},
                 headers={"Content-Type": "application/json","Authorization":self.createToken(playwight,user_credentials)})
        assert response.ok
        print(response.json())
        return response.json()["orders"][0]