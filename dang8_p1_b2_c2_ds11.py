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


def bt_dang8_p1_b2_c2_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                x=symbols('x')
                a=randint(1,30)
                c=3*a

                du = [
                    '$%s$' %(latex(Rational(5*a,4))),
                    ]
                da= random.choice(du)
                s = [
                    '$%s$' %(latex(Rational(5*a,4)+1)),
                    '$%s$' %(latex(Rational(5*a,4)+2)),
                    '$%s$' %(latex(Rational(5*a,4)+3)),
                    '$%s$' %(latex(Rational(5*a,4)-1)),
                    '$%s$' %(latex(Rational(5*a,4)-2)),
                    '$%s$' %(latex(Rational(5*a,4)-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Một tam giác vuông có chu vi bằng $%s$ và ba cạnh lập thành một cấp số cộng. Độ dài cạnh dài nhất là   \n'
                                %(latex(c)
                                    )
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Gọi $x, y, z$ theo thứ tự tăng dần là độ dài ba cạnh của tam giác $(x, y, z >0)$. \\\\ \n'
                        'Chu vi tam giác $ABC$ là $x+y+z=%s$ \\hspace*{1cm} (1). \\\\ \n'
                        'Ba cạnh lập thành một cấp số cộng nên là $x+z=2y$ \\hspace*{1cm} (2). \\\\ \n'
                        'Tam giác là tam giác vuông nên $x^2+y^2=z^2$ \\hspace*{1cm} (3). \\\\ \n'
                        'Thay (2) vào (1) được $3y=%s \\Leftrightarrow y=%s$. \\\\ \n'
                        'Thay $y=%s$ vào (2) ta được $x+z=%s \\Leftrightarrow x=%s-z$. \\\\ \n'
                        'Thay $x$ và $y$ vào (3) ta được \\\\ \n'
                        '\\hspace*{1cm} $(%s-z)^2+%s^2=z^2 \\Leftrightarrow z=%s$, suy ra $x=%s$. \\\\ \n'
                        'Vậy độ dài ba cạnh của tam giác thỏa mãn yêu cầu lần lượt là $%s; %s; %s$.'

                        %(latex(c),
                        latex(c),latex(a),
                        latex(a),latex(2*a),latex(2*a),
                        latex(2*a),latex(a),latex(Rational(5*a,4)),latex(Rational(3*a,4)),
                        latex(Rational(3*a,4)),latex(a),latex(Rational(5*a,4)),
                        ))
            if dang=='1':
                x=symbols('x')
                a=randint(1,20)
                c=3*a

                du = [
                    '$%s$' %(latex(Rational(3*a,4))),
                    ]
                da= random.choice(du)
                s = [
                    '$%s$' %(latex(Rational(3*a,4)+1)),
                    '$%s$' %(latex(Rational(3*a,4)+2)),
                    '$%s$' %(latex(Rational(3*a,4)+3)),
                    '$%s$' %(latex(Rational(3*a,4)-1)),
                    '$%s$' %(latex(Rational(3*a,4)-2)),
                    '$%s$' %(latex(Rational(3*a,4)-3)),
                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Một tam giác vuông có chu vi bằng $%s$ và ba cạnh lập thành một cấp số cộng. Độ dài cạnh ngắn nhất là   \n'
                                %(latex(c)
                                    )
                                )

                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Gọi $x, y, z$ theo thứ tự tăng dần là độ dài ba cạnh của tam giác $(x, y, z >0)$. \\\\ \n'
                        'Chu vi tam giác là $x+y+z=%s$ \\hspace*{1cm} (1). \\\\ \n'
                        'Ba cạnh lập thành một cấp số cộng nên là $x+z=2y$ \\hspace*{1cm} (2). \\\\ \n'
                        'Tam giác là tam giác vuông nên $x^2+y^2=z^2$ \\hspace*{1cm} (3). \\\\ \n'
                        'Thay (2) vào (1) được $3y=%s \\Leftrightarrow y=%s$. \\\\ \n'
                        'Thay $y=%s$ vào (2) ta được $x+z=%s \\Leftrightarrow x=%s-z$. \\\\ \n'
                        'Thay $x$ và $y$ vào (3) ta được \\\\ \n'
                        '\\hspace*{1cm} $(%s-z)^2+%s^2=z^2 \\Leftrightarrow z=%s$, suy ra $x=%s$. \\\\ \n'
                        'Vậy độ dài ba cạnh của tam giác thỏa mãn yêu cầu lần lượt là $%s; %s; %s$.'

                        %(latex(c),
                        latex(c),latex(a),
                        latex(a),latex(2*a),latex(2*a),
                        latex(2*a),latex(a),latex(Rational(5*a,4)),latex(Rational(3*a,4)),
                        latex(Rational(3*a,4)),latex(a),latex(Rational(5*a,4)),
                        ))    
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n '+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('.0', '')
            return content

