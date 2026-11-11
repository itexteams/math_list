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


def bt_dang14_p4_b3_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $O$ là giao điểm của hai đường chéo hình bình hành. Một mặt phẳng $(P)$ qua $O$ đồng thời song song với $SA$ và $CD$. Tìm thiết diện tạo bởi mặt phẳng $(P)$ và hình chóp. \n')
        loigiai = ('\\begin{center} \n'
                   '\\begin{tikzpicture}[>=stealth,scale=1, line join = round, line cap = round] \n'
                   '\\tkzDefPoints{0/0/D, 5/0/C, 2/1.5/A} \n'
                   '\\coordinate (B) at ($(A)+(C)-(D)$); \n'
                   '\\coordinate (S) at ($(A)+(1,3)$); \n'
                   '\\tkzInterLL(A,C)(B,D) \\tkzGetPoint{O} \n'
                   '\\tkzDefLine[parallel=through O](C,D) \\tkzGetPoint{o} \n'
                   '\\tkzInterLL(O,o)(A,D) \\tkzGetPoint{M} \n'
                   '\\tkzInterLL(O,o)(B,C) \\tkzGetPoint{N} \n'
                   '\\tkzDefLine[parallel=through O](S,A) \\tkzGetPoint{o1} \n'
                   '\\tkzInterLL(O,o1)(S,C) \\tkzGetPoint{P} \n'
                   '\\tkzDefLine[parallel=through P](C,D) \\tkzGetPoint{p1} \n'
                   '\\tkzInterLL(P,p1)(S,D) \\tkzGetPoint{Q} \n'
                   '\\tkzDrawSegments(S,D S,C S,B D,C C,B N,P P,Q) \n'
                   '\\tkzDrawSegments[dashed](S,A A,D A,B A,C B,D M,N O,P Q,M) \n'
                   '\\tkzFillPolygon[black, opacity=0.3](M,N,P,Q) \n'
                   '\\tkzDrawPoints(S,A,B,C,D,O,M,N,P,Q) \n'
                   '\\tkzLabelPoints[above](S) \n'
                   '\\tkzLabelPoints[below](D,O) \n'
                   '\\tkzLabelPoints[left](A,Q) \n'
                   '\\tkzLabelPoints[right](C,B,N) \n'
                   '\\tkzLabelPoints[below left](M) \n'
                   '\\tkzLabelPoints[above right](P) \n'
                   '\\end{tikzpicture} \n'
                   '\\end{center} \n'
                   'Mặt phẳng $(SAC)$ chứa đường thẳng $SA$ song song với mặt phẳng $(P)$ nên mặt phẳng $(SAC)$ cắt mặt phẳng $(P)$ theo giao tuyến song song với $SA$. \n'
                   'Qua $O$ kẻ $OP \\parallel SA, (P \\in SC)$ thì $PO$ là giao tuyến của mặt phẳng $(P)$ và mặt phẳng $(SAC)$. \n'
                   'Mặt phẳng $(ABCD)$ chứa đường thẳng $CD$ song song với mặt phẳng $(P)$ nên mặt phẳng $(ABCD)$ cắt mặt phẳng $(P)$ theo giao tuyến song song với $CD$. \n'
                   'Qua $O$ kẻ $MN \\parallel CD, (M \\in AD, N \\in BC)$ thì $MN$ là giao tuyến của mặt phẳng $(P)$ và mặt phẳng $(ABCD)$. \n'
                   'Mặt phẳng $(SCD)$ chứa đường thẳng $CD$ song song với mặt phẳng $(P)$ nên mặt phẳng $(SCD)$ cắt mặt phẳng $(P)$ theo giao tuyến song song với $CD$. \n'
                   'Kẻ $PQ \\parallel CD, (Q \\in SD)$ thì $PQ$ là giao tuyến của mặt phẳng $(P)$ và mặt phẳng $(SCD)$. \n'
                   'Khi đó giao tuyến của mặt phẳng $(SAD)$ với mặt phẳng $(P)$ là $QM$. \n'
                   'Khi đó giao tuyến của mặt phẳng $(SCB)$ với mặt phẳng $(P)$ là $PN$. \n'
                   'Tứ giác $MNPQ$ có $MN \\parallel PQ$ (vì cùng song song với $CD$) nên nó là hình thang. \n')

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+
               '\\loigiai{ \n'
               +str(loigiai)+'}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content  

