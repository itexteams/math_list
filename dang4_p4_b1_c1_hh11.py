import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang4_p4_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,9)


                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$, có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M, N, P$ lần lượt là trung điểm của $BC, CD, SO$. Tìm giao tuyến của $(MNP)$ với mặt phẳng $(SAB)$.'''
                                 %(
                                 ))

                # Nội dung lời giải
                loigiai = (    '''\\begin{center}
            	\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
            		\\clip(-2.457734848488052,-1.3857672579795268) rectangle (6.47621890510299,3.470154835001351);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (-2.,-1.);
            		\\draw [line width=1.pt ] (-2.,-1.)-- (2.,-1.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (2.,-1.)-- (4.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (0.,3.);
            		\\draw [line width=1.pt ] (0.,3.)-- (-2.,-1.);
            		\\draw [line width=1.pt ] (0.,3.)-- (2.,-1.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,3.)-- (4.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,-1.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (-2.,-1.)-- (4.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,3.)-- (1.,-0.5);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,-1.)-- (6.,0.);
            		\\draw [line width=1.pt ] (0.,3.)-- (6.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (6.,0.)-- (4.,0.);
            		\\draw [line width=1.pt ] (6.,0.)-- (2.,-1.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,-1.)-- (2.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,3.)-- (2.,0.);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,-1.)-- (0.7599028490453973,1.8554428768984865);
            		\\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.7599028490453973,1.8554428768984865)-- (6.,0.);
            		\\draw (-0.2,3.6) node[anchor=north west] {$S$};
            		\\draw (-0.5,0.40573798020759333) node[anchor=north west] {$A$};
            		\\draw (3.9,0.4764552922412954) node[anchor=north west] {$B$};
            		\\draw (1.9031660602569158,-0.890746073743612) node[anchor=north west] {$C$};
            		\\draw (-2.5,-0.8082425430376262) node[anchor=north west] {$D$};
            		\\draw (0.8541925984236668,-0.4192973268522646) node[anchor=north west] {$O$};
            		\\draw (2.869635991384179,-0.3485800148185625) node[anchor=north west] {$M$};
            		\\draw (-0.25371195677100067,-0.9143185110881794) node[anchor=north west] {$N$};
            		\\draw (0,1.3486354739902882) node[anchor=north west] {$P$};
            		\\draw (1.9974558096351855,0.4646690735690117) node[anchor=north west] {$E$};
            		\\draw (6.087273688917628,0.26430335614018907) node[anchor=north west] {$G$};
            		\\draw (0.7363304117008299,2.2915329677729828) node[anchor=north west] {$F$};
            	\\end{tikzpicture}
            \\end{center}
            Gọi $E=NO \\cap AB; F=NP \\cap SE; G=MN \\cap AB$. Ta có \\\\
                           $\\heva{&G \\in AB \\Rightarrow G \\in (SAB) \\\\& F \\in SE \\subset (SAB) \\Rightarrow F \\in (SAB)} \\Rightarrow GF \\subset (SAB).$ \\\\
                            $\\heva{&G \\in MN \\Rightarrow G \\in (MNP) \\\\& F \\in NP \\Rightarrow F \\in (MNP)} \\Rightarrow GF \\subset (MNP).$ \\\\
                                Vậy $GF=(SAB) \\cap (MNP)$.'''

                           %(
                           ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

