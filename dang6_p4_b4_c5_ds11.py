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


def bt_dang6_p4_b4_c5_ds11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lisa=[300,350,400,450,500,550,600,650]
                a=random.choice(lisa)
                n=randint(4,9)
                k=randint(50000000,100000000)
                t=a*1000000+k
                r=round((t/(a*1000000))**(1/n)-1,5)
                h1=r  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
                r0=kq*100

                # Nội dung câu hỏi
                noidungcauhoi = ('Để đầu tư dự án trồng rau sạch theo công nghệ mới, một người đã làm hợp đồng xin vay '
                                'vốn ngân hàng số tiền là $%s$ triệu đồng với lãi suất $r$ cho kỳ hạn một năm$zz$ Điều kiện kèm theo của hợp đồng là số tiền lãi năm trước sẽ được tính làm vốn để sinh lãi cho năm sau '
                                '(theo thể thức lãi kép)$zz$ Sau $%s$ năm thành công với dự án rau sạch của mình, '
                                'người đó đã thanh toán hợp đồng ngân hàng với số tiền là $%s$ đồng$zz$ '
                                'Tìm lãi suất ngân hàng mỗi năm$zz$ (làm tròn kết quả đến hàng phần chục)$zz$'
                                %(latex(a),latex(n),latex(t)
                                ))

                # Nội dung lời giải
                loigiai = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $A=%s$ triệu đồng$zz$ \\\\ \n'
                        '\\hspace*{1cm} Lãi suất $r$ một năm$zz$ \\\\ \n'
                        '\\hspace*{1cm} Kỳ hạn $n=%s$ năm$zz$ \\\\ \n'
                        '\\hspace*{1cm} Số tiền $T=%s$ đồng$zz$ \\\\ \n'
                        'Theo công thức lãi kép ta có \\\\ \n'
                        '\\hspace*{1cm} $T=A(1+r)^n \\Leftrightarrow %s=%s(1+r)^%s \\Leftrightarrow r=\\sqrt[%s]{%s}-1 \\approx %s$$zz$ \\\\ \n'
                        'Vậy lãi suất vay ngân hàng là $%s$ phần trăm mỗi năm$zz$'

                        %(latex(a*1000000),
                            latex(n),
                            latex(t),latex(t),latex(a*1000000),latex(n),latex(n),latex(Rational(t,a*1000000)),latex(kq),
                            latex(r0)
                            ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('00}', '}').replace('phần trăm', '\\%').replace('.', ',').replace('$zz$', '.')
            return content 

