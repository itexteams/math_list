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


def bt_dang19_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$. Gọi $E$ là điểm nằm giữa $A, C$. Mặt phẳng $(P)$ qua $E$ và song song với hai đường thẳng $AB,CD$. Xác định giao tuyến của $(P)$ với các mặt của hình chóp. Hình tạo bởi các giao tuyến là hình gì? \n')
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[>=stealth,scale=1, line join = round, line cap = round] \n'
                   '\\tkzDefPoints{0/0/B, 6/0/D, 2/-3/C, 1/3/A} \n'
                   '\\coordinate (E) at ($(A)!0.6!(C)$); \n'
                   '\\tkzDefLine[parallel=through E](A,B) \\tkzGetPoint{e1} \n'
                   '\\tkzInterLL(E,e1)(B,C) \\tkzGetPoint{F} \n'
                   '\\tkzDefLine[parallel=through F](C,D) \\tkzGetPoint{f1} \n'
                   '\\tkzInterLL(F,f1)(B,D) \\tkzGetPoint{G} \n'
                   '\\tkzDefLine[parallel=through E](C,D) \\tkzGetPoint{e2} \n'
                   '\\tkzInterLL(E,e2)(A,D) \\tkzGetPoint{H} \n'
                   '\\tkzDrawSegments(A,B A,C A,D B,C C,D E,F F,G) \n'
                   '\\tkzDrawSegments[dashed](B,D E,H G,H) \n'
                   '\\tkzFillPolygon[black, opacity=0.3](E,F,G,H) \n'
                   '\\tkzDrawPoints(A,B,C,D,E,F,G,H) \n'
                   '\\tkzLabelPoints[above](A,H) \n'
                   '\\tkzLabelPoints[below](C) \n'
                   '\\tkzLabelPoints[left](B,E,F) \n'
                   '\\tkzLabelPoints[right](D) \n'
                   '\\tkzLabelPoints[below right](G) \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Mặt phẳng $(ABC)$ chứa đường thẳng $AB$ song song với mặt phẳng $(P)$ nên mặt phẳng $(ABC)$ cắt mặt phẳng $(P)$ theo giao tuyến song song với $AB$. \n'
                   'Kẻ $EF \\parallel AB, (F \\in BC)$ thì $EF$ là giao tuyến của mặt phẳng $(P)$ và mặt phẳng $(ABC)$. \n'
                   'Hai mặt phẳng $(ACD)$ và $(BCD)$ cùng chứa đường thẳng $CD$ song song với mặt phẳng $(P)$ nên cắt mặt phẳng $(P)$ theo giao tuyến song song với $CD$. Kẻ $EH, FG$ lần lượt là giao tuyến của mặt phẳng $(P)$ và hai mặt phẳng $(ACD)$ và $(BCD)$. Khi đó $GH$ là giao tuyến của mặt phẳng $(P)$ và mặt phẳng $(ABD)$. \n'
                   'Mặt phẳng $(ABD)$ chứa đường thẳng $AB$ song song với mặt phẳng $(P)$ nên $GH \\parallel AB$. \n'
                   'Tứ giác $EFGH$ có $EF \\parallel GH$ (vì cùng song song với $AB$) và $EH \\parallel FG$ (vì cùng song song với $CD$) nên nó là hình bình hành. \n')
    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+
               '\\loigiai{ \n'
               +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content  

