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


def bt_dang1_p3_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(4,20)
                b=randint(2,9)
                bm=Rational(b*a,b+1)
                bn=Rational(a,2)
                mn=sqrt(bm**2+bn**2-2*bm*bn*cos(pi/3))
                ih=Rational(a,2*2)-Rational(a,2*b+1*2)
                jh=sqrt(mn**2-ih**2)
                dientich=(Rational(a,b+1)+Rational(a,2))*jh/2
                h1=dientich    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$ có tất cả các cạnh bằng $%s$, $I$ là trung điểm của $AC$, $J$ là một điểm trên cạnh $AD$ sao cho $AJ=%s JD$. $(P)$ là mặt phẳng chứa $IJ$ và song song với $AB$. Diện tích của hình tạo bởi các giao tuyến của tứ diện và mặt phẳng $(P)$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)  \n'
                                %(latex(a),latex(b)
                                ))

                # Nội dung lời giải
                loigiai = ('\\begin{center}  \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\clip(-0.6874467271680568,-2.623609510267522) rectangle (5.6636913772655975,4.874754657723026); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.); \n'
                            '\\draw [line width=1.pt] (0.,0.)-- (2.,-2.); \n'
                            '\\draw [line width=1.pt] (2.,-2.)-- (5.,0.); \n'
                            '\\draw [line width=1.pt] (2.,-2.)-- (1.,4.); \n'
                            '\\draw [line width=1.pt] (1.,4.)-- (0.,0.); \n'
                            '\\draw [line width=1.pt] (1.,4.)-- (5.,0.); \n'
                            '\\draw [line width=1.pt] (0.5,2.)-- (1.,-1.); \n'
                            '\\draw [line width=1.pt] (3.728276993593576,1.271723006406424)-- (4.046207745195182,-0.635861503203212); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.5,2.)-- (3.728276993593576,1.271723006406424); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,-1.)-- (4.046207745195182,-0.635861503203212); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.625,1.25)-- (3.728276993593576,1.271723006406424); \n'
                            '\\draw (0.7081478656125227,4.685521492600236) node[anchor=north west] {$A$}; \n'
                            '\\draw (1.8435468563492654,-1.9494663595175834) node[anchor=north west] {$B$}; \n'
                            '\\draw (-0.5336947805057896,0.34498576759624355) node[anchor=north west] {$C$}; \n'
                            '\\draw (5.143300173177924,0.34498576759624355) node[anchor=north west] {$D$}; \n'
                            '\\draw (4.114344837822751,-0.5183905482764851) node[anchor=north west] {$M$}; \n'
                            '\\draw (0.3,-0.8495485872413673) node[anchor=north west] {$N$}; \n'
                            '\\draw (0.11679422460380262,2.4502047295872806) node[anchor=north west] {$I$}; \n'
                            '\\draw (3.818668017318391,1.882505234218911) node[anchor=north west] {$J$}; \n'
                            '\\draw (0.6,1.2911515932101927) node[anchor=north west] {$H$}; \n'
                        '\\end{tikzpicture}  \n'
                    '\\end{center}  \n'

                            'Mặt phẳng $(P)$ chứa $IJ$ và song song với $AB$ nên $(P)$ cắt $BD$ và $BC$ lần lượt tại $M$ và $N$ sao cho $IN, AB$ và $JM$ đôi một song song. \\\\ \n'
                        'Hình tạo bởi $(P)$ và tứ diện là tứ giác $IJMN$. \\\\ \n'
                        'Vì $IN // JM$ nên tứ giác $IJMN$ là hình thang cân và có $IN=\\dfrac{1}{2}AB=%s; JM=\\dfrac{1}{%s}AB=%s$. \\\\ \n'
                        'Ta có \\\\ \n'
                        '\\hspace*{1cm} $IJ=MN=\\sqrt{BM^2+BN^2-2BM \\cdot BN \\cos 60^\\circ}$ \\\\ \n'
                        '\\hspace*{1cm} $IJ=MN=\\sqrt{\\left(%s\\right)^2+\\left(%s\\right)^2-2 \\cdot %s \\cdot %s \\cdot %s}=%s$. \\\\ \n'
                        'Gọi $JH$ là đường cao của hình thang, ta có \\\\ \n'
                        '\\hspace*{1cm} $IH=\\dfrac{IN-JM}{2}=%s$. \\\\ \n'
                        '\\hspace*{1cm} $JH=\\sqrt{IJ^2-IH^2}=\\sqrt{\\left(%s\\right)^2-\\left(%s\\right)^2}=%s$. \\\\ \n'
                        'Diện tích hình thang $IJMN$ là \\\\ \n'
                        '\\hspace*{1cm} $S=\\dfrac{1}{2}(JM+IN)JH=\\dfrac{1}{2}(%s+%s)%s =%s \\approx %s$. \\\\ \n'

                        %(latex(Rational(a,2)),latex(b+1),latex(Rational(a,b+1)),
                            latex(bm),latex(bn),latex(bm),latex(bn),latex(Rational(1,2)),latex(mn),
                            latex(ih),
                            latex(mn),latex(ih),latex(jh),
                            latex(Rational(a,b+1)),latex(Rational(a,2)),latex(jh),latex(dientich),latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

