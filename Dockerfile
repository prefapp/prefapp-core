FROM python AS BUILD

WORKDIR /prefapp-core

COPY . .

RUN python setup.py bdist_wheel

FROM python

WORKDIR /prefapp-core

COPY --from=BUILD /prefapp-core/dist .

RUN pip3 install *.whl
