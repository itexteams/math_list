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


def bt_dang2_p4_b2_c3_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                k1=randint(1,10)
                k2=randint(1,10)
                k3=randint(1,10)
                k4=randint(1,10)

                x1=randint(1,20)
                x2=x1+k1
                x3=x2+k2
                x4=x3+k3
                x5=x4+k4

                m1=randint(1,20)
                m2=randint(1,20)
                m3=randint(1,20)
                m4=randint(1,20)
                m5=randint(1,20)

                n=m1+m2+m3+m4+m5

                h1=(m1*x1+m2*x2+m3*x3+m4*x4+m5*x5)/n


                xtb = Decimal(float(h1)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


                # Nội dung câu hỏi
                noidungcauhoi = ('Thống kê số chai nhựa mà các bạn học sinh thu gom trong đợt phát động vệ sinh bảo vệ môi trường được cho trong bảng sau \n'
                                '''\\begin{center}
                                \\begin{tabular}{|c|c|c|c|c|c|}
                                    \\hline
                                    Số chai nhựa & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\, & \\, $%s$ \\,  \\\\
                                    \\hline
                                    Số học sinh & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\
                                    \\hline
                                \\end{tabular}
                                \\end{center}'''
                                'Tìm số trung bình của mẫu số liệu$zz$'

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                                latex(m1),latex(m2),latex(m3),latex(m4),latex(m5),
                                ))

                # Nội dung lời giải
                loigiai=('Số học sinh là $n=%s+%s+%s+%s+%s=%s$$zz$\\\\ \n'
                        'Trung bình mỗi bạn đọc số cuốn sách là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s+%s \\cdot %s}{%s }=%s$$zz$'
                        %(latex(m1),latex(m2),latex(m3),latex(m4),latex(m5),latex(n),
                            latex(m1),latex(x1),latex(m2),latex(x2),latex(m3),latex(x3),latex(m4),latex(x4),latex(m5),latex(x5),latex(n),
                        latex(xtb)
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

