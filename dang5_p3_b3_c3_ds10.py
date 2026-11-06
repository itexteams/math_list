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


def bt_dang5_p3_b3_c3_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Giá trị và tần số
                x1=randint(1,20)
                x2=randint(1,20)
                x3=randint(1,20)
                x4=randint(1,20)
                x5=randint(1,20)
                x6=randint(1,20)


                xtb=Rational(x1+x2+x3+x4+x5+x6,6)
                tb = Decimal(float((x1+x2+x3+x4+x5+x6)/6)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

                #Phương sai
                s2=Rational((x1-xtb)**2+(x2-xtb)**2+(x3-xtb)**2+(x4-xtb)**2+(x5-xtb)**2+(x6-xtb)**2,6)
                #Độ lệch
                ss=sqrt(s2)

                dl = Decimal(float(ss)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu \n'
                                '$$%s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s$$'
                                'Độ lệch chuẩn của mẫu số liệu bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)$zz$'

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6)
                                ))

                # Nội dung lời giải
                loigiai=('Số trung bình của mẫu số liệu là \\\\ \n'
                        '$\\bar{x}=\\dfrac{%s+%s+%s+%s+%s+%s}{6}=%s$$zz$ \\\\ \n'
                        'Phương sai của mẫu số liệu là \\\\ \n'
                        '$s^2=\\dfrac{\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2+\\left(%s-%s\\right)^2}{6}$ \\\\ \n'
                        '\\hspace*{0.35cm} $=%s$$zz$ \\\\ \n'
                        'Độ lệch chuẩn của mẫu số liệu là \\\\ \n'
                        '$s=\\sqrt{s^2}=\\sqrt{%s}=%s \\approx %s$$zz$'
                        %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),
                        latex(xtb),

                            latex(x1),latex(xtb),latex(x2),latex(xtb),latex(x3),latex(xtb),latex(x4),latex(xtb),latex(x5),latex(xtb),latex(x6),latex(xtb),
                        latex(s2),
                        latex(s2),latex(ss),latex(dl)

                        ))


                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(dl))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('0}', '}')
            return content

