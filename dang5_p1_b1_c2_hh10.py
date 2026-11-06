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


def bt_dang5_p1_b1_c2_hh10(self):
            # Khai báo biến
            a=randint(2,9)
            b=randint(2,9)
            c=sqrt(a**2+b**2)

            lisi=[1,2,3,-1,-2,-3]
            i1=random.choice(lisi)
            lisi.remove(i1)
            i2=random.choice(lisi)
            lisi.remove(i2)
            i3=random.choice(lisi)

            c1=sqrt(a**2+b**2+i1)
            c2=sqrt(a**2+b**2+i2)
            c3=sqrt(a**2+b**2+i3)

            lis=['1','2','3','4']
            dang=random.choice(lis)
            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('Cho tam giác $ABC$ vuông tại $A$, có $AB=%s, AC=%s$. Độ dài vectơ $\\overrightarrow{BC}$ là \n'
                            %(latex(a),latex(b)
                            ))    
                # Các đáp án
                da_d = '\\True $\\left| \\overrightarrow{BC} \\right|=%s$' %(latex(c))
                da_s1 = '$\\left| \\overrightarrow{BC} \\right|=%s$' %(latex(c1))
                da_s2 = '$\\left| \\overrightarrow{BC} \\right|=%s$' %(latex(c2))
                da_s3 = '$\\left| \\overrightarrow{BC} \\right|=%s$' %(latex(c3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí Pythagore cho tam giác $ABC$ ta có \\\\ \n'
                        '$BC=\\sqrt{AB^2+AC^2}=\\sqrt{%s^2+%s^2}=%s$. \\\\ \n'
                        'Vậy độ dài vectơ $\\overrightarrow{BC}$ là $%s$.'
                        %(latex(a),latex(b),latex(c),latex(c))
                        )
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('Cho tam giác $ABC$ vuông tại $A$, có $AB=%s, BC=%s$. Độ dài vectơ $\\overrightarrow{AC}$ là \n'
                            %(latex(a),latex(c)
                            ))    
                # Các đáp án
                da_d = '\\True $\\left| \\overrightarrow{AC} \\right|=%s$' %(latex(b))
                da_s1 = '$\\left| \\overrightarrow{AC} \\right|=%s$' %(latex(b+1))
                da_s2 = '$\\left| \\overrightarrow{AC} \\right|=%s$' %(latex(b-1))
                da_s3 = '$\\left| \\overrightarrow{AC} \\right|=%s$' %(latex(b+2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí Pythagore cho tam giác $ABC$ ta có \\\\ \n'
                        '$AC=\\sqrt{BC^2-AB^2}=\\sqrt{%s-%s}=%s$. \\\\ \n'
                        'Vậy độ dài vectơ $\\overrightarrow{AC}$ là $%s$.'
                        %(latex(a**2+b**2),latex(a**2),latex(b),latex(b))
                        )
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('Cho tam giác $ABC$ vuông tại $A$, có $AC=%s, BC=%s$. Độ dài vectơ $\\overrightarrow{AB}$ là \n'
                            %(latex(b),latex(c)
                            ))    
                # Các đáp án
                da_d = '\\True $\\left| \\overrightarrow{AB} \\right|=%s$' %(latex(a))
                da_s1 = '$\\left| \\overrightarrow{AB} \\right|=%s$' %(latex(a+1))
                da_s2 = '$\\left| \\overrightarrow{AB} \\right|=%s$' %(latex(a-1))
                da_s3 = '$\\left| \\overrightarrow{AB} \\right|=%s$' %(latex(a+2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí Pythagore cho tam giác $ABC$ ta có \\\\ \n'
                        '$AB=\\sqrt{BC^2-AC^2}=\\sqrt{%s-%s}=%s$. \\\\ \n'
                        'Vậy độ dài vectơ $\\overrightarrow{AB}$ là $%s$.'
                        %(latex(a**2+b**2),latex(b**2),latex(a),latex(a))
                        )  
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('Cho tam giác $ABC$ vuông tại $A$, có $AB=%s, AC=%s$, $M$ là trung điểm cạnh $BC$. Độ dài vectơ $\\overrightarrow{AM}$ là \n'
                            %(latex(a),latex(b)
                            ))    
                # Các đáp án
                da_d = '\\True $\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(c/2))
                da_s1 = '$\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(c1/2))
                da_s2 = '$\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(c2/2))
                da_s3 = '$\\left| \\overrightarrow{AM} \\right|=%s$' %(latex(c3/2))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí Pythagore cho tam giác $ABC$ ta có \\\\ \n'
                        '$BC=\\sqrt{AB^2+AC^2}=\\sqrt{%s^2+%s^2}=%s$. \\\\ \n'
                        'Vậy độ dài vectơ $\\overrightarrow{AM}$ là $%s$.'
                        %(latex(a),latex(b),latex(c),latex(c/2))
                        )  
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'} \n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac')
            return content

