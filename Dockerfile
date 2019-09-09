FROM google/cloud-sdk:slim

RUN git clone https://github.com/cuiran/highdim_preprocessing.git /home/prep-sumstats/
RUN git clone https://github.com/bulik/ldsc.git /home/ldsc/
RUN chmod 777 -R /home/prep-sumstats/
RUN chmod 777 -R /home/ldsc/

COPY requirements.txt /home/

RUN pip install -r /home/requirements.txt 

VOLUME ["/root/.config"]
CMD ["/bin/bash"]
