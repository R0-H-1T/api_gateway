# API GATEWAY

---
## Quizz Application


#### Plan of work
Client credentials flow




**Changes to be made**
1. Split the `Auth` service -> `Token` + `Auth`Service
2. Add Git Submodule (pydantic models for `qna`, `auth` and `analytics`)
3. CORS Middleware?



> Notes
1. Global Dependencies - Ex: `verify-token` applied to all the path operaitons of the application


```python
app = FastAPI(dependencies=[Depends(get_query_token)])
```

**To run locally, set env**
```
AUTH_PORT=8081
QNA_PORT=8082
ANALYTICS_PORT=8083
```
