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


def bt_dang16_p1_b2_c2_hh10(self):
            # Khai báo biến
            a=randint(2,30)
            lis0=[30,45,60,90,120,135,150]
            goc=random.choice(lis0)
            goc_rad=goc*pi/180
            goc1=180-goc
            goc1_rad=goc1*pi/180

            kq11=sqrt(a**2+a**2-2*a*a*cos(goc1_rad))
            kq12=kq11
            kq1=round(kq12,1)

            kq22=sqrt(a**2+a**2-2*a*a*cos(goc_rad))
            kq21=kq22
            kq2=round(kq21,1)

            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='1':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hình thoi $ABCD$ cạnh bằng $%s a$, góc $\\widehat{BAD}=%s^\\circ$$zz$ Độ dài vectơ $\\overrightarrow{AB}+\\overrightarrow{AD}$ là \n'
                                %(latex(a),latex(goc)
                                ))
                # Các đáp án
                da_d = '\\True $%s a$'%(latex(kq1))
                da_s1 = '$%s a$'%(latex(kq1+0.1))
                da_s2 = '$%s a$'%(latex(kq1-0.1))
                da_s3 = '$%s a$'%(latex(kq1+0.2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Ta có $\\widehat{ABC}=180^\\circ-%s^\\circ=%s^\\circ$$zz$ \\\\ \n'
                        'Áp dụng định lí cosin cho tam giác $ABC$: \\\\ \n'
                        '$AC=\\sqrt{AB^2+BC^2-2AB \\cdot BC \\cos %s^\\circ}=\\sqrt{%s a^2+%s a^2-2 \\cdot %s a \\cdot %s a \\cdot \\cos %s^\\circ} =%s a$ \\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\left| \\overrightarrow{AB}+\\overrightarrow{AD} \\right|=\\left| \\overrightarrow{AC} \\right| =AC=%s a=%s a$$zz$'
                        %(latex(goc),latex(goc1),
                        latex(goc1),latex(a**2),latex(a**2),latex(a),latex(a),latex(goc1),latex(kq11),
                        latex(kq12),latex(kq1)
                        ))
            if dang=='2':
                #Nội ung câu hỏi
                noidungcauhoi = ('Cho hình thoi $ABCD$ cạnh bằng $%s a$, góc $\\widehat{BAD}=%s^\\circ$$zz$ Độ dài vectơ $\\overrightarrow{BA}+\\overrightarrow{BC}$ là  \n'
                                %(latex(a),latex(goc)
                                ))
                # Các đáp án
                da_d = '\\True $%s a$'%(latex(kq2))
                da_s1 = '$%s a$'%(latex(kq2-0.1))
                da_s2 = '$%s a$'%(latex(kq2-0.2))
                da_s3 = '$%s a$'%(latex(kq2-0.3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=(
                        'Áp dụng định lí cosin cho tam giác $ABD$: \\\\ \n'
                        '$BD=\\sqrt{AB^2+AD^2-2AB \\cdot AD \\cos %s^\\circ}=\\sqrt{%s a^2+%s a^2-2 \\cdot %s a \\cdot %s a \\cdot \\cos %s^\\circ} =%s a$ \\\\ \n'
                        'Ta có \\\\ \n'
                        '$\\left| \\overrightarrow{BA}+\\overrightarrow{BC} \\right|=\\left| \\overrightarrow{BD} \\right| =BD=%s a=%s a$$zz$'
                        %(latex(goc),
                        latex(a**2),latex(a**2),latex(a),latex(a),latex(goc),latex(kq22),
                        latex(kq21),latex(kq2)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('.',',').replace('$zz$','.')
            return content

