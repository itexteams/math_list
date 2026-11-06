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


def bt_dang2_p3_b1_c2_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)

            if dang=='3':
                a=randint(2,9)
                goc1=atan(1)
                goc=goc1*180/pi

                h1=goc 
                number = Decimal(float(h1))  # Số cần làm tròn
                gocz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''                     
                                Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, các tam giác $SAB$, $SAD$, $SAC$ là các giác vuông tại $A$. Biết $SA=%s$, $AD=%s$. Góc giữa hai đường thẳng $SD$ và $BC$ bằng bao nhiêu?
                                '''
                                %(latex(a),latex(a)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-4.36,-3.34) rectangle (6.36,5.3);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (-3.,-2.);
                    \\draw [line width=1.pt] (-3.,-2.)-- (2.,-2.);
                    \\draw [line width=1.pt] (2.,-2.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (0.,4.);
                    \\draw [line width=1.pt] (0.,4.)-- (5.,0.);
                    \\draw [line width=1.pt] (0.,4.)-- (-3.,-2.);
                    \\draw [line width=1.pt] (0.,4.)-- (2.,-2.);
                    \\draw (-0.26,4.6) node[anchor=north west] {$S$};
                    \\draw (-0.6,0.66) node[anchor=north west] {$A$};
                    \\draw (-3.54,-1.8) node[anchor=north west] {$B$};
                    \\draw (1.98,-1.86) node[anchor=north west] {$C$};
                    \\draw (5,0.52) node[anchor=north west] {$D$};
                \\end{tikzpicture}
            \\end{center}
                        Để xác định góc giữa hai đường thẳng $SD$ và $BC$ ta tìm đường thẳng song song với một trong hai đường thẳng $SD$, $BC$ và song song với một đường thẳng còn lại.\\\\
                    Ta dễ nhận thấy $AD//BC$.\\\\
                    Khi đó $\\left(SD,BC\\right)=\\left(SD,AD\\right)=\\hoac{ &\\widehat{SDA}\\\\ &180^\\circ-\\widehat{SDA}}$. \\\\
                    Xét $\\triangle SAD$ có $\\tan \\widehat{SDA}=\\dfrac{SA}{AD}=1$ suy ra $\\widehat{SAD}=%s^\\circ$. \\\\
                    Vậy $\\left(SD,BC\\right)=%s^\\circ$.'''
                        %(latex(goc),latex(goc)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(goc))
            if dang=='2':
                a=randint(2,9)
                goc1=atan(sqrt(3)/1)
                goc=goc1*180/pi

                h1=goc 
                number = Decimal(float(h1))  # Số cần làm tròn
                gocz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''                     
                                Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, các tam giác $SAB$, $SAD$, $SAC$ là các giác vuông tại $A$. Biết $SA=%s \\sqrt{3}$, $AD=%s$. Góc giữa hai đường thẳng $SD$ và $BC$ bằng bao nhiêu?
                                '''
                                %(latex(a),latex(a)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-4.36,-3.34) rectangle (6.36,5.3);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (-3.,-2.);
                    \\draw [line width=1.pt] (-3.,-2.)-- (2.,-2.);
                    \\draw [line width=1.pt] (2.,-2.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (0.,4.);
                    \\draw [line width=1.pt] (0.,4.)-- (5.,0.);
                    \\draw [line width=1.pt] (0.,4.)-- (-3.,-2.);
                    \\draw [line width=1.pt] (0.,4.)-- (2.,-2.);
                    \\draw (-0.26,4.6) node[anchor=north west] {$S$};
                    \\draw (-0.6,0.66) node[anchor=north west] {$A$};
                    \\draw (-3.54,-1.8) node[anchor=north west] {$B$};
                    \\draw (1.98,-1.86) node[anchor=north west] {$C$};
                    \\draw (5,0.52) node[anchor=north west] {$D$};
                \\end{tikzpicture}
            \\end{center}
                        Để xác định góc giữa hai đường thẳng $SD$ và $BC$ ta tìm đường thẳng song song với một trong hai đường thẳng $SD$, $BC$ và song song với một đường thẳng còn lại.\\\\
                    Ta dễ nhận thấy $AD//BC$.\\\\
                    Khi đó $\\left(SD,BC\\right)=\\left(SD,AD\\right)=\\hoac{ &\\widehat{SDA}\\\\ &180^\\circ-\\widehat{SDA}}$. \\\\
                    Xét $\\triangle SAD$ có $\\tan \\widehat{SDA}=\\dfrac{SA}{AD}=\\dfrac{\\sqrt{3}}{1}=\\sqrt{3}$ suy ra $\\widehat{SAD}=%s^\\circ$. \\\\
                    Vậy $\\left(SD,BC\\right)=%s^\\circ$.'''
                        %(latex(goc),latex(goc)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(goc))

            if dang=='1':
                a=randint(2,9)
                goc1=atan(1/sqrt(3))
                goc=goc1*180/pi

                h1=goc 
                number = Decimal(float(h1))  # Số cần làm tròn
                gocz = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''                     
                                Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, các tam giác $SAB$, $SAD$, $SAC$ là các giác vuông tại $A$. Biết $SA=%s \\sqrt{3}$, $AD=%s$. Góc giữa hai đường thẳng $SD$ và $BC$ bằng bao nhiêu?
                                '''
                                %(latex(a),latex(3*a)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-4.36,-3.34) rectangle (6.36,5.3);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (-3.,-2.);
                    \\draw [line width=1.pt] (-3.,-2.)-- (2.,-2.);
                    \\draw [line width=1.pt] (2.,-2.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (0.,4.);
                    \\draw [line width=1.pt] (0.,4.)-- (5.,0.);
                    \\draw [line width=1.pt] (0.,4.)-- (-3.,-2.);
                    \\draw [line width=1.pt] (0.,4.)-- (2.,-2.);
                    \\draw (-0.26,4.6) node[anchor=north west] {$S$};
                    \\draw (-0.6,0.66) node[anchor=north west] {$A$};
                    \\draw (-3.54,-1.8) node[anchor=north west] {$B$};
                    \\draw (1.98,-1.86) node[anchor=north west] {$C$};
                    \\draw (5,0.52) node[anchor=north west] {$D$};
                \\end{tikzpicture}
            \\end{center}
                        Để xác định góc giữa hai đường thẳng $SD$ và $BC$ ta tìm đường thẳng song song với một trong hai đường thẳng $SD$, $BC$ và song song với một đường thẳng còn lại.\\\\
                    Ta dễ nhận thấy $AD//BC$.\\\\
                    Khi đó $\\left(SD,BC\\right)=\\left(SD,AD\\right)=\\hoac{ &\\widehat{SDA}\\\\ &180^\\circ-\\widehat{SDA}}$. \\\\
                    Xét $\\triangle SAD$ có $\\tan \\widehat{SDA}=\\dfrac{SA}{AD}=\\dfrac{\\sqrt{3}}{3}$ suy ra $\\widehat{SAD}=30^\\circ$. \\\\
                    Vậy $\\left(SD,BC\\right)=30^\\circ$.'''
                        %(
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(goc))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content                


