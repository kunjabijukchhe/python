{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "Could not find PyAudio; check installation",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/speech_recognition/__init__.py\u001b[0m in \u001b[0;36mget_pyaudio\u001b[0;34m()\u001b[0m\n\u001b[1;32m    107\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 108\u001b[0;31m             \u001b[0;32mimport\u001b[0m \u001b[0mpyaudio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    109\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mImportError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pyaudio'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-ce44ff323290>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mRecognizer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mwith\u001b[0m \u001b[0msr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mMicrophone\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0msource\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Speak Anything :\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0maudio\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlisten\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msource\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/speech_recognition/__init__.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, device_index, sample_rate, chunk_size)\u001b[0m\n\u001b[1;32m     77\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     78\u001b[0m         \u001b[0;31m# set up PyAudio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 79\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyaudio_module\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_pyaudio\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     80\u001b[0m         \u001b[0maudio\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyaudio_module\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mPyAudio\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     81\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/speech_recognition/__init__.py\u001b[0m in \u001b[0;36mget_pyaudio\u001b[0;34m()\u001b[0m\n\u001b[1;32m    108\u001b[0m             \u001b[0;32mimport\u001b[0m \u001b[0mpyaudio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    109\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mImportError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 110\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Could not find PyAudio; check installation\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    111\u001b[0m         \u001b[0;32mfrom\u001b[0m \u001b[0mdistutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mversion\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpyaudio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__version__\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"0.2.11\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: Could not find PyAudio; check installation"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "\n",
    "r = sr.Recognizer()\n",
    "with sr.Microphone() as source:\n",
    "    print(\"Speak Anything :\")\n",
    "    audio = r.listen(source)\n",
    "    try:\n",
    "        text = r.recognize_gimport speech_recognition as sr\n",
    "\n",
    "r = sr.Recognizer()\n",
    "with sr.Microphone() as source:\n",
    "    print(\"Speak Anything :\")\n",
    "    audio = r.listen(source)\n",
    "    try:\n",
    "        text = r.recognize_google(audio)\n",
    "        print(\"You said : {}\".format(text))\n",
    "    except:\n",
    "        print(\"Sorry could not recognize what you said\")oogle(audio)\n",
    "        print(\"You said : {}\".format(text))\n",
    "    except:\n",
    "        print(\"Sorry could not recognize what you said\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "Could not find PyAudio; check installation",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/speech_recognition/__init__.py\u001b[0m in \u001b[0;36mget_pyaudio\u001b[0;34m()\u001b[0m\n\u001b[1;32m    107\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 108\u001b[0;31m             \u001b[0;32mimport\u001b[0m \u001b[0mpyaudio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    109\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mImportError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pyaudio'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-ce44ff323290>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mr\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mRecognizer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mwith\u001b[0m \u001b[0msr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mMicrophone\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0msource\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Speak Anything :\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0maudio\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlisten\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msource\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/speech_recognition/__init__.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, device_index, sample_rate, chunk_size)\u001b[0m\n\u001b[1;32m     77\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     78\u001b[0m         \u001b[0;31m# set up PyAudio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 79\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyaudio_module\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_pyaudio\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     80\u001b[0m         \u001b[0maudio\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpyaudio_module\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mPyAudio\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     81\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/speech_recognition/__init__.py\u001b[0m in \u001b[0;36mget_pyaudio\u001b[0;34m()\u001b[0m\n\u001b[1;32m    108\u001b[0m             \u001b[0;32mimport\u001b[0m \u001b[0mpyaudio\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    109\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mImportError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 110\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Could not find PyAudio; check installation\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    111\u001b[0m         \u001b[0;32mfrom\u001b[0m \u001b[0mdistutils\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mversion\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    112\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpyaudio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__version__\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0mLooseVersion\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"0.2.11\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: Could not find PyAudio; check installation"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "\n",
    "r = sr.Recognizer()\n",
    "with sr.Microphone() as source:\n",
    "    print(\"Speak Anything :\")\n",
    "    audio = r.listen(source)\n",
    "    try:\n",
    "        text = r.recognize_google(audio)\n",
    "        print(\"You said : {}\".format(text))\n",
    "    except:\n",
    "        print(\"Sorry could not recognize what you said\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
