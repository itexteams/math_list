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


def bt_dang10_p1_b2_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                du = ['$90^\\circ$',
                    ]
                da= random.choice(du)
                s = ['$60^\\circ$',
                    '$30^\\circ$',
                    '$0^\\circ$',
                    '$45^\\circ$',
                    '$70^\\circ$',
                    '$20^\\circ$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''\\immini{Cho biết cột trụ gôn của một sân bóng đá là đường thẳng vuông góc với mặt sân. Góc giữa cột trụ gôn và một đường thẳng bất kỳ nằm trên sân là
                                }{
                                    \\definecolor{eqeqeq}{rgb}{0.8784313725490196,0.8784313725490196,0.8784313725490196}
                                    \\definecolor{ffxfqq}{rgb}{1.,0.4980392156862745,0.}
                                    \\definecolor{ffffff}{rgb}{1.,1.,1.}
                                    \\definecolor{qqwuqq}{rgb}{0.,0.39215686274509803,0.}
                                    \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.1428300613982949,-0.08499033906526406) rectangle (5.11770366131563,3.6000201258433617);
                    \\fill[line width=2.pt,color=qqwuqq,fill=qqwuqq,fill opacity=1.0] (0.,1.5) -- (5.,1.5) -- (5.,0.) -- (0.0033718775234579113,-0.0010730093796875728) -- cycle;
                    \\fill[line width=0.pt,color=ffxfqq,fill=ffxfqq,fill opacity=1.0] (0.,1.5) -- (0.,3.5) -- (5.,3.5) -- (5.,1.5) -- cycle;
                    \\fill[line width=0.8pt,color=ffffff,fill=ffffff,pattern=north east lines,pattern color=ffffff] (0.8789528045423797,2.4266178668921357) -- (1.4920225241067846,2.6837116202578537) -- (1.5198917094221338,0.607078658723177) -- (0.5493454284324847,0.7192516586428797) -- cycle;
                    \\fill[line width=2.pt,color=ffffff,fill=ffffff,pattern=north east lines,pattern color=ffffff] (4.115697237941549,2.4925393421141147) -- (3.5685489935991233,2.2420377362705946) -- (3.318047387755603,0.9302003793532124) -- (4.1168417379308275,0.9002870888151856) -- cycle;
                    \\fill[line width=2.pt,color=eqeqeq,fill=eqeqeq,pattern=north east lines,pattern color=eqeqeq] (1.4920225241067846,2.6837116202578537) -- (4.115697237941549,2.4925393421141147) -- (3.5685489935991233,2.2420377362705946) -- (3.318047387755603,0.9302003793532124) -- (0.5493454284324847,0.7192516586428797) -- (0.8789528045423797,2.4266178668921357) -- cycle;
                    \\draw [line width=1.6pt,color=qqwuqq] (0.,1.5)-- (5.,1.5);
                    \\draw [line width=1.6pt,color=qqwuqq] (5.,1.5)-- (5.,0.);
                    \\draw [line width=1.6pt,color=qqwuqq] (5.,0.)-- (0.0033718775234579113,-0.0010730093796875728);
                    \\draw [line width=1.6pt,color=qqwuqq] (0.0033718775234579113,-0.0010730093796875728)-- (0.,1.5);
                    \\draw [line width=1.6pt,color=ffffff] (5.,1.)-- (0.002390647485514967,0.43574532571757346);
                    \\draw [line width=1.6pt,color=ffffff] (0.0028792763047730714,0.21822036311417956)-- (3.3378238303221965,0.04026046385649603);
                    \\draw [line width=1.6pt,color=ffffff] (3.3378238303221965,0.04026046385649603)-- (5.,0.32372280731100567);
                    \\draw [line width=1.6pt,color=ffffff] (1.4920225241067846,2.6837116202578537)-- (4.115697237941549,2.4925393421141147);
                    \\draw [line width=1.6pt,color=ffffff] (4.1168417379308275,0.9002870888151856)-- (3.318047387755603,0.9302003793532124);
                    \\draw [line width=1.6pt,color=ffffff] (3.318047387755603,0.9302003793532124)-- (0.5493454284324847,0.7192516586428797);
                    \\draw [line width=1.6pt,color=ffffff] (0.5493454284324847,0.7192516586428797)-- (1.5198917094221338,0.607078658723177);
                    \\draw [line width=1.6pt,color=ffffff] (1.4920225241067846,2.6837116202578537)-- (0.8789528045423797,2.4266178668921357);
                    \\draw [line width=1.6pt,color=ffffff] (4.115697237941549,2.4925393421141147)-- (3.5685489935991233,2.2420377362705946);
                    \\draw [line width=1.6pt,color=ffxfqq] (0.,1.5)-- (0.,3.5);
                    \\draw [line width=1.6pt,color=ffxfqq] (0.,3.5)-- (5.,3.5);
                    \\draw [line width=1.6pt,color=ffxfqq] (5.,1.5)-- (0.,1.5);
                    \\draw [line width=1.6pt,color=ffffff] (0.8789528045423797,2.4266178668921357)-- (0.5493454284324847,0.7192516586428797);
                    \\draw [line width=1.6pt,color=ffffff] (1.4920225241067846,2.6837116202578537)-- (1.5198917094221338,0.607078658723177);
                    \\draw [line width=1.6pt,color=ffffff] (4.115697237941549,2.4925393421141147)-- (4.1168417379308275,0.9002870888151856);
                    \\draw [line width=1.6pt,color=ffffff] (3.5685489935991233,2.2420377362705946)-- (3.318047387755603,0.9302003793532124);
                    \\draw [line width=1.6pt,color=ffffff] (0.8789528045423797,2.4266178668921357)-- (1.4920225241067846,2.6837116202578537);
                    \\draw [line width=1.6pt,color=ffffff] (1.4920225241067846,2.6837116202578537)-- (1.5198917094221338,0.607078658723177);
                    \\draw [line width=1.6pt,color=ffffff] (1.5198917094221338,0.607078658723177)-- (0.5493454284324847,0.7192516586428797);
                    \\draw [line width=1.6pt,color=ffffff] (0.5493454284324847,0.7192516586428797)-- (0.8789528045423797,2.4266178668921357);
                    \\draw [line width=1.6pt,color=ffffff] (4.115697237941549,2.4925393421141147)-- (3.5685489935991233,2.2420377362705946);
                    \\draw [line width=1.6pt,color=ffffff] (3.5685489935991233,2.2420377362705946)-- (3.318047387755603,0.9302003793532124);
                    \\draw [line width=1.6pt,color=ffffff] (3.318047387755603,0.9302003793532124)-- (4.1168417379308275,0.9002870888151856);
                    \\draw [line width=1.6pt,color=ffffff] (4.1168417379308275,0.9002870888151856)-- (4.115697237941549,2.4925393421141147);
                    \\draw [line width=1.6pt,color=eqeqeq] (1.4920225241067846,2.6837116202578537)-- (4.115697237941549,2.4925393421141147);
                    \\draw [line width=1.6pt,color=eqeqeq] (4.115697237941549,2.4925393421141147)-- (3.5685489935991233,2.2420377362705946);
                    \\draw [line width=1.6pt,color=eqeqeq] (3.5685489935991233,2.2420377362705946)-- (3.318047387755603,0.9302003793532124);
                    \\draw [line width=1.6pt,color=eqeqeq] (3.318047387755603,0.9302003793532124)-- (0.5493454284324847,0.7192516586428797);
                    \\draw [line width=1.6pt,color=eqeqeq] (0.5493454284324847,0.7192516586428797)-- (0.8789528045423797,2.4266178668921357);
                    \\draw [line width=1.6pt,color=eqeqeq] (0.8789528045423797,2.4266178668921357)-- (1.4920225241067846,2.6837116202578537);
                    \\end{tikzpicture}}  '''
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Do cột trụ gôn vuông góc với mặt sân nên suy ra nó vuông góc với mọi đường nằm trong sân. Vậy góc giữa cột trụ gôn và một đường thẳng bất kỳ nằm trong sân là $90^\\circ$.'''
                        %(
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

