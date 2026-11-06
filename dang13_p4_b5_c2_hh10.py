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


def bt_dang13_p4_b5_c2_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(1,9)
                b=randint(1,9)
                c=randint(1,9)
                m=randint(1,9)
                n=randint(-9,-1)
                p=randint(1,9)
                q=randint(-9,-1)


                x0=(m*p*a**2+(m*q+n*p)*c+n*q*b**2)/((sqrt(m**2*a**2+2*m*n*c+n**2*b**2))*(sqrt(p**2*a**2+2*p*q*c+q**2*b**2)))
                while m**2*a**2+2*m*n*c+n**2*b**2<=0 or p**2*a**2+2*p*q*c+q**2+b**2<=0:
                    a=randint(1,9)
                    b=randint(1,9)
                    c=randint(1,9)
                    m=randint(1,9)
                    n=randint(-9,-1)
                    p=randint(1,9)
                    q=randint(-9,-1)


                    x0=(m*p*a**2+(m*q+n*p)*c+n*q*b**2)/((sqrt(m**2*a**2+2*m*n*c+n**2*b**2))*(sqrt(p**2*a**2+2*p*q*c+q**2+b**2)))


                number = Decimal(float(x0))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hai vectơ $\\vec{a},\\vec{b}$ thỏa $\\left|\\vec{a}\\right|=%s$, $\\left|\\vec{b}\\right|=%s$, $\\vec{a}\\cdot\\vec{b}=%s$$zz$ Xét hai vectơ $\\vec{x}=%s\\vec{a}+%s\\vec{b}$, $\\vec{y}=%s\\vec{a}+%s\\vec{b}$$zz$ Tính cosin góc giữa hai vectơ $\\vec{x}, \\vec{y}$$zz$ (Kết quả làm tròn đến hàng phần chục)$zz$'
                                %(latex(a),latex(b),latex(c),latex(m),latex(n),latex(p),latex(q))
                                )

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '$\\text{cos}(\\vec{x},\\vec{y})=\\dfrac{\\vec{x}\\cdot\\vec{y}}{|\\vec{x}|\\cdot |\\vec{y}|}$$zz$ Trong đó \\\\ \n'
                        '\\hspace*{1cm}$\\bullet \\vec{x}\\cdot\\vec{y}=(%s\\vec{a}+%s\\vec{b})(%s\\vec{a}+%s\\vec{b})=%s\\vec{a}^2+%s\\vec{a}\\vec{b}+%s\\vec{b}^2$$zz$\\\\ \n'

                        '\\hspace*{1cm}$\\bullet |\\vec{x}|=|%s\\vec{a}+%s\\vec{b}|\\Rightarrow |\\vec{x}|^2=|%s\\vec{a}+%s\\vec{b}|^2=%s\\vec{a}^2+%s\\vec{a}\\vec{b}+%s\\vec{b}^2$ \\\\ \n'
                        '\\hspace*{4.3cm}$\\Rightarrow|\\vec{x}|=\\sqrt{%s\\vec{a}^2+%s\\vec{a}\\vec{b}+%s\\vec{b}^2}$$zz$ \\\\ \n'

                        '\\hspace*{1cm}$\\bullet |\\vec{y}|=|%s\\vec{a}+%s\\vec{b}|\\Rightarrow |\\vec{y}|^2=|%s\\vec{a}+%s\\vec{b}|^2=%s\\vec{a}^2+%s\\vec{a}\\vec{b}+%s\\vec{b}^2$ \\\\ \n'
                        '\\hspace*{4.3cm}$\\Rightarrow|\\vec{y}|=\\sqrt{%s\\vec{a}^2+%s\\vec{a}\\vec{b}+%s\\vec{b}^2}$$zz$ \\\\ \n'

                        '\\hspace*{1cm}$\\bullet \\vec{a}^2=|\\vec{a}|^2=%s; \\vec{b}^2=|\\vec{b}|^2=%s; \\vec{a}\\cdot\\vec{b}=%s$$zz$ \\\\ \n'

                        '$\\text{Cos}(\\vec{x},\\vec{y})=\\dfrac{%s\\cdot%s+%s\\cdot%s+%s\\cdot%s}{\\sqrt{%s\\cdot%s+%s\\cdot%s+%s\\cdot%s}\\sqrt{%s\\cdot%s+%s\\cdot%s+%s\\cdot%s}} =%s \\approx %s$$zz$'
                            %(latex(m),latex(n),latex(p),latex(q),latex(m*p),latex(m*q+n*p),latex(n*q),

                            latex(m),latex(n),latex(m),latex(n),latex(m**2),latex(2*m*n),latex(n**2),
                            latex(m**2),latex(2*m*n),latex(n**2),

                            latex(p),latex(q),latex(p),latex(q),latex(p**2),latex(2*p*q),latex(q**2),
                            latex(p**2),latex(2*p*q),latex(q**2),

                            latex(a**2),latex(b**2),latex(c),

                            latex(m*p),latex(a**2),latex(m*q+n*p),latex(c),latex(n*q),latex(b**2),latex(m**2),latex(a**2),latex(2*m*n),latex(c),latex(n**2),latex(b**2),latex(p**2),latex(a**2),latex(2*p*q),latex(c),latex(q**2),latex(b**2),latex(x0),latex(kq),
                            )
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('+-', '-').replace('--', '+').replace('21\\vec', '21f\\vec').replace('51\\vec', '51f\\vec').replace('81\\vec', '81f\\vec').replace('1\\vec', '\\vec').replace('21f\\vec', '21\\vec').replace('51f\\vec', '51\\vec').replace('81f\\vec', '81\\vec')
            return content 

