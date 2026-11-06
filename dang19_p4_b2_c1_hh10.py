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


def bt_dang19_p4_b2_c1_hh10(self):
            # Khai báo biến
            lis0=[10,15,20,25,30,35,40,45,50,55,60,65]
            goc1=random.choice(lis0)
            goc1_rad=goc1 * pi / 180

            goc2=random.choice(lis0)
            goc2_rad=goc2 * pi / 180

            goc3=180-goc1-goc2
            goc3_rad=goc3 * pi / 180

            lis1=[2,3,4,5,6,7,8,9]
            a=random.choice(lis1)
            b=random.choice(lis1)
            c=random.choice(lis1)

            kq1=round(c*sin(goc1_rad)/sin(goc2_rad),1)
            kq1s1=round(kq1+0.1,1)
            kq1s2=round(kq1+0.2,1)
            kq1s3=round(kq1-0.1,1)

            kq2=round(c*sin(goc1_rad)/sin(goc3_rad),1)
            kq2s1=round(kq2+0.1,1)
            kq2s2=round(kq2+0.2,1)
            kq2s3=round(kq2-0.1,1)

            kq3=round(c/(2*sin(goc3_rad)),1)
            kq3s1=round(kq3+0.1,1)
            kq3s2=round(kq3+0.2,1)
            kq3s3=round(kq3-0.1,1)

            lis=['1','2','3']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $\\widehat{A} = %s^\\circ, \\widehat{B} = %s^\\circ$ và $AB=%s$$zzz$ Tính độ dài cạnh $BC$.'''
                            %(latex(goc1),latex(goc2),latex(c)
                            ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(kq1))
                da_s1 = '$%s$' %(latex(kq1s1))
                da_s2 = '$%s$' %(latex(kq1s2))
                da_s3 = '$%s$' %(latex(kq1s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\widehat{C} = 180^\\circ - \\widehat{A} - \\widehat{B} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                        'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                        '$\\dfrac{AB}{\\sin C} = \\dfrac{BC}{\\sin A}$ suy ra $BC = \\dfrac{AB \\sin A}{\\sin C} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$ \\\\ \n'
                        %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                        latex(c), latex(goc1), latex(goc2),latex(kq1)
                        ))
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $\\widehat{B} = %s^\\circ, \\widehat{C} = %s^\\circ$ và $BC=%s$$zzz$ Tính độ dài cạnh $CA$.'''
                            %(latex(goc1),latex(goc2),latex(c)
                            ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(kq2))
                da_s1 = '$%s$' %(latex(kq2s1))
                da_s2 = '$%s$' %(latex(kq2s2))
                da_s3 = '$%s$' %(latex(kq2s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\widehat{A} = 180^\\circ - \\widehat{B} - \\widehat{C} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                        'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                        '$\\dfrac{CA}{\\sin B} = \\dfrac{BC}{\\sin A}$ suy ra $CA = \\dfrac{BC \\sin B}{\\sin A} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$ \\\\ \n'
                        %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                        latex(c), latex(goc1), latex(180-goc1-goc2),latex(kq2)
                        ))
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Cho tam giác $ABC$ có $\\widehat{C} = %s^\\circ, \\widehat{A} = %s^\\circ$ và $CA=%s$$zzz$ Tính độ dài cạnh $AB$.'''
                            %(latex(goc1),latex(goc2),latex(c)
                            ))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(kq2))
                da_s1 = '$%s$' %(latex(kq2s1))
                da_s2 = '$%s$' %(latex(kq2s2))
                da_s3 = '$%s$' %(latex(kq2s3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Góc $\\widehat{B} = 180^\\circ - \\widehat{C} - \\widehat{A} = 180^\\circ -%s^\\circ -%s^\\circ = %s^\\circ$$zzz$\\\\ \n'
                        'Áp dụng định lí sin cho tam giác $ABC$, ta có \\\\ \n'
                        '$\\dfrac{AB}{\\sin C} = \\dfrac{CA}{\\sin B}$ suy ra $AB = \\dfrac{CA \\sin C}{\\sin B} = \\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx  %s$$zzz$ \\\\ \n'
                        %(latex(goc1),latex(goc2),latex(180-goc1-goc2),
                        latex(c), latex(goc1), latex(180-goc1-goc2),latex(kq2)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('.',',').replace('$zzz$','.').replace('{,}0','')
            return content

