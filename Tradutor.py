{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "olá\n",
      "olá\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "denovo = 'a'\n",
    "while denovo == 'a':\n",
    "\t\t\n",
    "\turl = \"https://google-translate1.p.rapidapi.com/language/translate/v2\"\n",
    "\ttexto = str(input('Digite a frase que deseja traduzir: \\n'))\n",
    "\n",
    "\tpayload = {\n",
    "\t\t\"q\": f'{texto}',\n",
    "\t\t\"target\": \"pt\",\n",
    "\t\t\"source\": \"en\"\n",
    "\t}\n",
    "\theaders = {\n",
    "\t\t\"content-type\": \"application/x-www-form-urlencoded\",\n",
    "\t\t\"Accept-Encoding\": \"application/gzip\",\n",
    "\t\t\"X-RapidAPI-Key\": \"2397504bfamshf76b496e3dc8f8cp194698jsn0164748ddab7\",\n",
    "\t\t\"X-RapidAPI-Host\": \"google-translate1.p.rapidapi.com\"\n",
    "\t}\n",
    "\n",
    "\tresponse = requests.post(url, data=payload, headers=headers)\n",
    "\n",
    "\ta = response.text.split(sep=\"{\")[3]\n",
    "\tprint(a.split(sep='\"')[3])\n",
    "\tdenovo = input(str(\"Aperte a e enter para realizar nova tradução\"))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
