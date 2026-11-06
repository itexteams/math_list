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


def bt_dang4_p3_b2_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(2,6)
                b=1
                lisc=[20,30,40,50]
                c=random.choice(lisc)
                d=randint(2,5)
                hsb=Rational(4*b-4*a,c)
                hsa=-Rational(4*b-4*a,c**2)
                hsc=a
                f=hsa*x**2+hsb*x+hsc
                r=Rational(c,12)
                f0=hsc
                f1=hsa*(1*r)**2+hsb*(1*r)+hsc
                f2=hsa*(2*r)**2+hsb*(2*r)+hsc
                f3=hsa*(3*r)**2+hsb*(3*r)+hsc
                f4=hsa*(4*r)**2+hsb*(4*r)+hsc
                f5=hsa*(5*r)**2+hsb*(5*r)+hsc
                f6=hsa*(6*r)**2+hsb*(6*r)+hsc
                f7=hsa*(7*r)**2+hsb*(7*r)+hsc
                f8=hsa*(8*r)**2+hsb*(8*r)+hsc
                f9=hsa*(9*r)**2+hsb*(9*r)+hsc
                f10=hsa*(10*r)**2+hsb*(10*r)+hsc
                f11=hsa*(11*r)**2+hsb*(11*r)+hsc
                f12=hsa*(12*r)**2+hsb*(12*r)+hsc

                kq1=f0+f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12
                kq=kq1*(1+Rational(d,100))
                while kq>9999:
                    x=symbols('x')
                    a=randint(2,6)
                    b=1
                    lisc=[20,30,40,50]
                    c=random.choice(lisc)
                    d=randint(2,5)
                    hsb=Rational(4*b-4*a,c)
                    hsa=-Rational(4*b-4*a,c**2)
                    hsc=a
                    f=hsa*x**2+hsb*x+hsc
                    r=Rational(c,12)
                    f0=hsc
                    f1=hsa*(1*r)**2+hsb*(1*r)+hsc
                    f2=hsa*(2*r)**2+hsb*(2*r)+hsc
                    f3=hsa*(3*r)**2+hsb*(3*r)+hsc
                    f4=hsa*(4*r)**2+hsb*(4*r)+hsc
                    f5=hsa*(5*r)**2+hsb*(5*r)+hsc
                    f6=hsa*(6*r)**2+hsb*(6*r)+hsc
                    f7=hsa*(7*r)**2+hsb*(7*r)+hsc
                    f8=hsa*(8*r)**2+hsb*(8*r)+hsc
                    f9=hsa*(9*r)**2+hsb*(9*r)+hsc
                    f10=hsa*(10*r)**2+hsb*(10*r)+hsc
                    f11=hsa*(11*r)**2+hsb*(11*r)+hsc
                    f12=hsa*(12*r)**2+hsb*(12*r)+hsc

                    kq1=f0+f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12
                    kq=2*kq1*(1+Rational(d,100))        

                h1=kq   
                number = Decimal(float(h1))  # Số cần làm tròn
                kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Chiếc cầu dây văng một nhịp được thiết kế hai bên thành cầu có dạng parabol và được cố định bằng các dây cáp song song như hình vẽ'
                                r'''\begin{center}
