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


def bt_dang9_p1_b2_c1_hh10(self):
            # Khai báo biến
            lis1=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
            a=random.choice(lis1)
            rds=random.choice([-2,2])
            rds1=random.choice([-1,1])
            x0=sqrt((a**2)*2)
            x02=Rational((a**2)*4,3)
            x03=sqrt(x02)
            rds=random.choice([-2,2])
            x1=a*sqrt(2)
            x2=(a+rds1)*sqrt(2)
            x3=a+rds1
            lis=['1','2','3','4','5','6']
            dang=random.choice(lis)

            if dang=='1':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\widehat{xOy}=30{}^\\circ$. Gọi $A,B$ lần lượt là hai điểm di động trên $Ox,Oy$ sao cho độ dài $AB=%s$. Độ dài lớn nhất của $OB$ là\n'''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(2*a))
                da_s1 = '$%s$' %(latex(2*a-1))
                da_s2 = '$%s$' %(latex(2*a+1))
                da_s3 = '$%s$' %(latex(2*a+rds))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $OAB$ ta có\\\\ \n'
                        ' $A{{B}^{2}}=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\cos30{}^\\circ \\\\ \n'
                        '\\Leftrightarrow %s=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\dfrac{\\sqrt{3}}{2}$\\\\ \n'
                        '$\\Leftrightarrow O{{A}^{2}}-\\sqrt{3}\\cdot OB\\cdot OA+O{{B}^{2}}-%s=0$. \\\\ \n'
                        'Coi phương trình trên một phương trình bậc hai ẩn $OA$. Để phương trình có nghiệm thì\\\\ \n'
                        '$\\Delta\\ge 0\\Leftrightarrow {{(-\\sqrt{3}OB)}^{2}}-4(O{{B}^{2}}-%s)\\ge 0\\Leftrightarrow O{{B}^{2}}\\le %s\\Leftrightarrow OB\\le %s$. \\\\ \n'
                        'Vậy $\\max OB=%s$. '
                        %(latex(a**2),latex(a**2),latex(a**2),latex((a**2)*4),latex(a*2),latex(a*2)))
            if dang=='2':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\widehat{xOy}=45{}^\\circ$. Gọi $A,B$ lần lượt là hai điểm di động trên $Ox,Oy$ sao cho độ dài $AB=%s$. Độ dài lớn nhất của $OB$ là\n'''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(x0))
                da_s1 = '$%s$' %(latex(a))
                da_s2 = '$%s$' %(latex(x2))
                da_s3 = '$%s$' %(latex(x3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $OAB$ ta có\\\\ \n'
                        '$A{{B}^{2}}=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\cos45{}^\\circ \\\\ \n'
                        '\\Leftrightarrow %s=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\dfrac{\\sqrt{2}}{2}$\\\\ \n'
                        '$\\Leftrightarrow O{{A}^{2}}-\\sqrt{2}\\cdot OB\\cdot OA+O{{B}^{2}}-%s=0$. \\\\ \n'
                        'Coi phương trình trên là một phương trình bậc hai ẩn $OA$.Để phương trình có nghiệm thì\\\\ \n'
                        '$\\Delta\\ge 0\\Leftrightarrow {{(-\\sqrt{2}OB)}^{2}}-4(O{{B}^{2}}-%s)\\ge 0\\Leftrightarrow O{{B}^{2}}\\le %s\\Leftrightarrow OB\\le %s$. \\\\ \n'
                        'Vậy $\\max OB=%s$. '
                        %(latex(a**2),latex(a**2),latex(a**2),latex((a**2)*2),latex(x0),latex(x0)))
            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\widehat{xOy}=60{}^\\circ$. Gọi $A,B$ lần lượt là hai điểm di động trên $Ox,Oy$ sao cho độ dài $AB=%s$. Độ dài lớn nhất của $OB$ là\n'''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(x03))
                da_s1 = '$%s$' %(latex(x03/sqrt(3)))
                da_s2 = '$%s$' %(latex(x03+1))
                da_s3 = '$%s$' %(latex(x03/sqrt(3)+rds))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $OAB$ ta có\\\\ \n'
                        '$A{{B}^{2}}=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\cos60{}^\\circ\\\\ \n'
                        '\\Leftrightarrow %s=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\dfrac{1}{2}$\\\\ \n'
                        '$\\Leftrightarrow O{{A}^{2}}-OB\\cdot OA+O{{B}^{2}}-%s=0$. \\\\ \n'
                        'Coi phương trình trên là một phương trình bậc hai ẩn $OA$.Để phương trình có nghiệm thì\\\\ \n'
                        '${{\\Delta }_{(*)}}\\ge 0\\Leftrightarrow {{(-OB)}^{2}}-4(O{{B}^{2}}-%s)\\ge 0\\Leftrightarrow O{{B}^{2}}\\le %s\\Leftrightarrow OB\\le %s$. \\\\ \n'
                        'Vậy $\\max OB=%s$. '
                        %(latex(a**2),latex(a**2),latex(a**2),latex(x02),latex(x03),latex(x03)))
            if dang=='4':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\widehat{xOy}=120{}^\\circ$. Gọi $A,B$ lần lượt là hai điểm di động trên $Ox,Oy$ sao cho độ dài $AB=%s$. Độ dài lớn nhất của $OB$ là\n'''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(x03))
                da_s1 = '$%s$' %(latex(x03/sqrt(3)))
                da_s2 = '$%s$' %(latex(x03+1))
                da_s3 = '$%s$' %(latex(x03/sqrt(3)+rds))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $OAB$ ta có\\\\ \n'
                        '$A{{B}^{2}}=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\cos120{}^\\circ\\\\ \n'
                        '\\Leftrightarrow %s=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\left(-\\dfrac{1}{2}\\right)$\\\\ \n'
                        '$\\Leftrightarrow O{{A}^{2}}+OB\\cdot OA+O{{B}^{2}}-%s=0$. \\\\ \n'
                        'Coi phương trình trên là một phương trình bậc hai ẩn $OA$.Để phương trình có nghiệm thì\\\\ \n'
                        '$\\Delta\\ge 0\\Leftrightarrow {{(OB)}^{2}}-4(O{{B}^{2}}-%s)\\ge 0\\Leftrightarrow O{{B}^{2}}\\le %s\\Leftrightarrow OB\\le %s$. \\\\ \n'
                        'Vậy $\\max OB=%s$. '
                        %(latex(a**2),latex(a**2),latex(a**2),latex(x02),latex(x03),latex(x03)))
            if dang=='5':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\widehat{xOy}=135{}^\\circ$. Gọi $A,B$ lần lượt là hai điểm di động trên $Ox,Oy$ sao cho độ dài $AB=%s$. Độ dài lớn nhất của $OB$ là\n'''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(x0))
                da_s1 = '$%s$' %(latex(a))
                da_s2 = '$%s$' %(latex(x2))
                da_s3 = '$%s$' %(latex(x3))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $OAB$ ta có\\\\ \n'
                        '$A{{B}^{2}}=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\cos135{}^\\circ\\\\ \n'
                        '\\Leftrightarrow %s=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\left(-\\dfrac{\\sqrt{2}}{2}\\right)$\\\\ \n'
                        '$\\Leftrightarrow O{{A}^{2}}+\\sqrt{2}\\cdot OB\\cdot OA+O{{B}^{2}}-%s=0$. \\\\ \n'
                        'Coi phương trình trên là một phương trình bậc hai ẩn $OA$.Để phương trình có nghiệm thì\\\\ \n'
                        '$\\Delta\\ge 0\\Leftrightarrow {{(\\sqrt{2}OB)}^{2}}-4(O{{B}^{2}}-%s)\\ge 0\\Leftrightarrow O{{B}^{2}}\\le %s\\Leftrightarrow OB\\le %s$. \\\\ \n'
                        'Vậy $\\max OB=%s$. '
                        %(latex(a**2),latex(a**2),latex(a**2),latex((a**2)*2),latex(x0),latex(x0)))
            if dang=='6':
                # Câu hỏi
                noidungcauhoi=('''Cho $\\widehat{xOy}=150{}^\\circ$. Gọi $A,B$ lần lượt là hai điểm di động trên $Ox,Oy$ sao cho độ dài $AB=%s$. Độ dài lớn nhất của $OB$ là\n'''
                            %(latex(a)))
                # Các đáp án
                da_d = '\\True $%s$' %(latex(2*a))
                da_s1 = '$%s$' %(latex(2*a-1))
                da_s2 = '$%s$' %(latex(2*a+1))
                da_s3 = '$%s$' %(latex(2*a+rds))
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Áp dụng định lí cosin cho tam giác $OAB$\\\\ \n'
                        '$A{{B}^{2}}=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\cos150{}^\\circ \\\\ \n'
                        '\\Leftrightarrow %s=O{{A}^{2}}+O{{B}^{2}}-2OA\\cdot OB\\cdot\\left(-\\dfrac{\\sqrt{3}}{2}\\right)$\\\\ \n'
                        '$\\Leftrightarrow O{{A}^{2}}+\\sqrt{3}\\cdot OB\\cdot OA+O{{B}^{2}}-%s=0$. \\\\ \n'
                        'Coi phương trình trên là một phương trình bậc hai ẩn $OA$.Để phương trình có nghiệm thì\\\\ \n'
                        '$\\Delta\\ge 0\\Leftrightarrow {{(\\sqrt{3}OB)}^{2}}-4(O{{B}^{2}}-%s)\\ge 0\\Leftrightarrow O{{B}^{2}}\\le %s\\Leftrightarrow OB\\le %s$. \\\\ \n'
                        'Vậy $\\max OB=%s$. '
                        %(latex(a**2),latex(a**2),latex(a**2),latex((a**2)*4),latex(a*2),latex(a*2)))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zzz$','.').replace('.00','').replace('\\frac','\\dfrac').replace('{,}0','')
            return content

