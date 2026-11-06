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


def bt_dang3_p1_b3_c1_hh12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a1=randint(-9,9)
                b1=randint(-9,9)
                c1=randint(-9,9)

                a2=randint(-9,9)
                b2=randint(-9,9)
                c2=randint(-9,9)

                a3=randint(-9,9)
                b3=randint(-9,9)
                c3=randint(-9,9)

                lisdiem1=['A','B','C','D']
                diem1=random.choice(lisdiem1)
                lisdiem2=['M','N','P','Q']
                diem2=random.choice(lisdiem2)
                lisdiem3=['H','K','S','R']
                diem3=random.choice(lisdiem3)

                xg=Rational(a1+a2+a3,3)
                yg=Rational(b1+b2+b3,3)
                zg=Rational(c1+c2+c3,3)
                d = [
                    '$\\left(%s;%s;%s \\right)$'%(latex(xg),latex(yg),latex(zg)),
                    ]
                da= random.choice(d)
                s = [
                    '$\\left(%s;%s;%s \\right)$'%(latex(Rational(a1+a2+a3,3)),latex(Rational(b1+b2+b3,3)),latex(Rational(c1+c2+c3+1,3))),
                    '$\\left(%s;%s;%s \\right)$'%(latex(Rational(a1+a2+a3,3)),latex(Rational(b1+b2+b3+1,3)),latex(Rational(c1+c2+c3+1,3))),
                    '$\\left(%s;%s;%s \\right)$'%(latex(Rational(a1+a2+a3+1,3)),latex(Rational(b1+b2+b3,3)),latex(Rational(c1+c2+c3+1,3))),
                    '$\\left(%s;%s;%s \\right)$'%(latex(Rational(a1+a2+a3,3)),latex(Rational(b1+b2+b3,3)),latex(Rational(c1+c2+c3-1,3))),
                    '$\\left(%s;%s;%s \\right)$'%(latex(Rational(a1+a2+a3,3)),latex(Rational(b1+b2+b3-2,3)),latex(Rational(c1+c2+c3+1,3))),
                    '$\\left(%s;%s;%s \\right)$'%(latex(Rational(a1+a2+a3-2,3)),latex(Rational(b1+b2+b3,3)),latex(Rational(c1+c2+c3+1,3))),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong không gian $Oxyz$, cho ba điểm $%s(%s;%s;%s), %s(%s;%s;%s)$ và $%s(%s;%s;%s)$. Trọng tâm của tam giác $%s%s%s$ có tọa độ là  \n'
                                %(str(diem1), latex(a1),latex(b1),latex(c1),str(diem2), latex(a2),latex(b2),latex(c2),str(diem3), latex(a3),latex(b3),latex(c3),str(diem1),str(diem2),str(diem3)
                                ) )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Gọi $G$ là trọng tâm của tam giác $%s%s%s$, ta có \\\\ \n'
                        '$\\heva{&x_G=\\dfrac{x_%s+x_%s+x_%s}{3} \\\\ & y_G=\\dfrac{y_%s+y_%s+y_%s}{3} \\\\ & z_G=\\dfrac{z_%s+z_%s+z_%s}{2}} \\Leftrightarrow \\heva{&x_I=\\dfrac{%s+(%s)+(%s)}{3} \\\\ & y_I=\\dfrac{%s+(%s)+(%s)}{3} \\\\ & z_I=\\dfrac{%s+(%s)+(%s)}{3}} \\Leftrightarrow \\heva{&x_G=%s \\\\ & y_G=%s \\\\ & z_G=%s.}$ \\\\ \n'
                        'Vậy trọng tâm của tam giác đã cho là $G \\left(%s;%s;%s \\right)$.'         
                        %(str(diem1),str(diem2),str(diem3),
                        str(diem1),str(diem2), str(diem3),str(diem1),str(diem2),str(diem3),str(diem1),str(diem2),str(diem3),
                        latex(a1),latex(a2),latex(a3),latex(b1),latex(b2),latex(b3),latex(c1),latex(c2),latex(c3),latex(xg),latex(yg),latex(zg),
                        latex(xg),latex(yg),latex(zg),
                        ))


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice[2] \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

