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


def bt_dang12_p4_b2_c3_hh10(self):
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                a=randint(-9,9)
                b=randint(-9,9)
                c=randint(-9,9)
                d=randint(-9,9)
                x0=randint(-9,9)
                y0=randint(-9,9)
                while a==0 or b==0 or c==0 or d==0 or a*d-b*c==0:
                    x=symbols('x')
                    y=symbols('y')
                    a=randint(-9,9)
                    b=randint(-9,9)
                    c=randint(-9,9)
                    d=randint(-9,9)
                    x0=randint(-9,9)
                    y0=randint(-9,9)

                d1=a*x+b*y-(a*x0+b*y0)
                d2=c*x+d*y-(c*x0+d*y0)
                k=Rational(a,c)
                # Câu hỏi
                noidungcauhoi = ('Trong mặt phẳng tọa độ $(Oxy)$, cho hai đường thẳng $d_1: %s=0$ và $d_2:%s=0$. Tìm giao điểm $M$ của $d_1$ và $d_2$. '
                                %(latex(d1),latex(d2))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có $d_1$ và $d_2$ lần lượt có vectơ pháp tuyến là $\\vec{n_1}=(%s;%s);\\vec{n_2}=(%s;%s)$.\\\\ \n'
                        'Dễ thấy $\\vec{n_1}\\ne k\\cdot \\vec{n_2}$ với $\\forall k\\ne 0$, suy ra $\\vec{n_1}$ và $\\vec{n_2}$ không cùng phương.\\\\ \n'
                        'Khi đó $d_1$ cắt $d_2$ tại điểm $M$.\\\\ \n'
                        ' Giải hệ phương trình $\\heva{& %s=0 \\\\ & %s=0}\\Leftrightarrow \\heva{& x=%s \\\\ & y=%s}$.\\\\ \n'
                        'Vậy $d_1$ cắt $d_2$ tại điểm $M(%s;%s)$.'
                        %(latex(a),latex(b),latex(c),latex(d),

                            latex(d1),latex(d2),latex(x0),latex(y0),
                            latex(x0),latex(y0),
                            )
                        )

                du = ['$M(%s;%s)$'%(latex(x0),latex(y0)),

                    ]
                da = random.choice(du)
                s = ['$M(%s;%s)$'%(latex(x0+1),latex(y0)),
                    '$M(%s;%s)$'%(latex(x0-1),latex(y0)),
                    '$M(%s;%s)$'%(latex(x0),latex(y0+1)),
                    '$M(%s;%s)$'%(latex(x0),latex(y0-1)),
                    '$M(%s;%s)$'%(latex(x0+1),latex(y0+1)),
                    '$M(%s;%s)$'%(latex(x0-1),latex(y0-1)),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2)
                da_s3 = str(das3)
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + str(noidungcauhoi) +
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('\\pm 0', '0').replace('1{x}', '{x}').replace('+0', '').replace('-0', '')
            return content 

