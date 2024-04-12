#!make
BACKEND = backend
FRONTEND = frontend

help:
	@echo "--------------------------HELP--------------------------"
	@echo "To startup the backend: make backend"
	@echo "To startup the frontend: make frontend"
	@echo "--------------------------------------------------------"

backend:
	cd $(BACKEND) && node --env-file=.env index

frontend:
	cd $(FRONTEND) && npm start

.PHONY: backend
.PHONY: frontend
.PHONY: help