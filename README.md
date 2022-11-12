# Apollo tutorial => Selenium Testing

Team Members:
1. Shivangi Shakya
2. Vaishnavi Bacha
3. Pavan Mathari


# Source Code Run

Run below commands in two different terminals: 

```bash
cd fullstack-tutorial/final/server && npm i && npm start
```
and

```bash
cd fullstack-tutorial/final/client && npm i && npm start
```
# Selenium Test Run

```bash
pip3 install -r requirements.txt
```

```bash
python3 -m unittest discover -p '*.py'
```


# Test Cases Summary:

Two websites for selenium tests:
1. server : run on http://localhost:4000
2. client : run on http://localhost:3000

## SERVER Test Cases:

serverTest.py -> HomePageTest  
    - test_title  
    - test_homepage_text  

## CLIENT Test Cases:
clientHomepageTest.py -> HomePageTest  
    - test_title  
    - test_login  

clientLoggedInPageTest.py -> LoggedInPageTest  
    - test_Heading2  
    - test_loggedin_email_id  
    - test_element_a1_text  
    - test_count_visible_elements  
    - test_get_loadmore_button  
    - test_get_home_button  
    - test_get_cart_button  
    - test_get_profile_button  
    - test_get_logout_button  

clientCartPageTest.py -> CartPageTest  
    - test_current_url  
    - test_get_page_heading  
    - test_get_page_email_id  
    - test_get_items_if_no_item  
    - test_redirect_to_home  
    - test_get_filled_cart  

clientProfilePageTest.py -> ProfilePageTest  
    - test_current_url  
    - test_get_page_heading  
    - test_get_page_email_id  
    - test_get_empty_trips  
    - test_redirect_to_home  
    - test_get_some_trip  
