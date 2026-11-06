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


def bt_dang1_p4_b1_c2_hh10(self):
            # Khai báo biến
            a=randint(2,50)
            c=sqrt(a**2+a**2)
            c1=c/2
            lis1=['OA','OB','OC','OD']
            vt1=random.choice(lis1)
            lis2=['AB','BC','CD','AD']
            vt2=random.choice(lis2)
            number = Decimal(float(c1))  # Số cần làm tròn
            kq1 = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            number = Decimal(float(c))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='1':


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình vuông $ABCD$ tâm $O$, có độ dài cạnh bằng $%s$. Tính độ dài vectơ $\\overrightarrow{%s}$. (Kết quả làm tròn đến hàng phần chục)\n'
                            %(latex(a), str(vt1)
                            ))   

                # Nội dung lời giải
                loigiai = ('Áp dụng định lí Pythagore cho tam giác vuông $ABC$ ta có \\\\ \n'
                        '\\hspace*{1cm}$AC=\\sqrt{AB^2+BC^2}=\\sqrt{%s^2+%s^2}=%s$. \\\\ \n'
                        'Suy ra $%s=\\dfrac{AC}{2}=%s$. \\\\ \n'
                        'Vậy $\\left|\\overrightarrow{%s}\\right|=%s=%s\\simeq %s$.'
                        %(latex(a),latex(a),latex(c),str(vt1),latex(c/2),str(vt1),str(vt1),latex(c/2),latex(kq1))
                        )

            if dang=='2':


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình vuông $ABCD$ tâm $O$, có độ dài cạnh bằng $%s$. Tính độ dài vectơ $\\overrightarrow{%s}$. \n'%(latex(a),str(vt2)
                            ))

                # Nội dung lời giải
                loigiai = ('Ta có $\\left|\\overrightarrow{%s}\\right|=%s = %s$.'
                        %(str(vt2),str(vt2),latex(a))
                        )


            if dang=='3':
                # Câu hỏi
                noidungcauhoi=('Cho hình vuông $ABCD$ tâm $O$, có độ dài cạnh bằng $%s$. Tính độ dài vectơ $\\overrightarrow{AC}$. (Kết quả làm tròn đến hàng phần chục). \n'
                            %(latex(a)
                            ))    

                # Nội dung lời giải
                loigiai=('Áp dụng định lí Pythagore cho tam giác vuông $ABC$ ta có \\\\ \n'
                        '\\hspace*{1cm}$AC=\\sqrt{AB^2+BC^2}=\\sqrt{%s^2+%s^2}=%s$. \\\\ \n'
                        'Vậy $\\left|\\overrightarrow{AC}\\right|=AC=%s\\simeq %s$.'
                        %(latex(a),latex(a),latex(c),latex(c),latex(kq))
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

