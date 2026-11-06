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


def bt_dang8_p3_b3_c5_ds10(self):
            # Khai báo biết
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Khai báo biến
                x=symbols('x')
                y=symbols('y')
                a=randint(-3,3)
                b=randint(-3,3)
                k=randint(1,4)

                while a==0 or b==0:
                    x=symbols('x')
                    y=symbols('y')
                    a=randint(-3,3)
                    b=randint(-3,3)
                    k=randint(1,4)
                ax=a*x
                A1=a**5
                A2=5*(a**4)*b
                A3=10*(a**3)*b**2
                A4=10*(a**2)*b**3
                A5=5*(a)*b**4
                A6=b**5

                bt=a*x+b
                #TỔ HỢP CHẬP k CỦA n PHẦN TỬ
                C = math.comb(5,k)
                hs=C*a**(5-k)*b**k

                # Câu hỏi
                noidungcauhoi = ('Hệ số của của số hạng chứa $x^%s$ trong khai triển $(%s+%s)^5$ bằng bao nhiêu?'
                                %(latex(5-k),latex(ax),latex(b))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có\\\\ \n'
                        '$(%s+%s)^4 =(%s x)^5+\\mathop{C}_{5}^{1}(%s x)^4(%s)+\\mathop{C}_{5}^{2}(%s x)^3(%s)^2+\\mathop{C}_{5}^{3}(%s x)^2(%s)^3+\\mathop{C}_{5}^{4}(%s x)(%s)^4+(%s)^5$.\\\\ \n'
                        ' \\hspace*{2cm}$=(%s)^5 x^5+5(%s)^4(%s)x^4+10(%s )^3(%s)^2x^3+10(%s )^2(%s)^3x^2+5(%s )(%s)^4 x+(%s)^5$.\\\\ \n'
                        ' \\hspace*{2cm}$ =%s x^5+%s x^4+%s x^3+%s x^2+%s x+%s$.\\\\ \n'

                        'Vậy hệ số của $x^%s$ là $%s$.'
                        %(latex(ax),latex(b),latex(a),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(b),
                            latex(a),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(a),latex(b),latex(b),
                            latex(A1),latex(A2),latex(A3),latex(A4),latex(A5),latex(A6),
                            latex(5-k),latex(hs),)
                        )
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(hs))

                du = ['$%s$'%(latex(hs))

                    ]
                da = random.choice(du)
                s = ['$%s$'%(latex(hs+1)),
                    '$%s$'%(latex(hs-1)),
                    '$%s$'%(latex(hs+2)),
                    '$%s$'%(latex(hs-2)),
                    '$%s$'%(latex(hs+3)),
                    '$%s$'%(latex(hs-3)),

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
                    '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+').replace('1x', 'x').replace('x^1', 'x').replace('\\mathop{C}', 'C')
            return content

