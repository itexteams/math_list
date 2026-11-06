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


def bt_dang26_p3_b1_c2_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        while True:
            x0 = randint(1, 4)
            y0 = randint(1, 4)
            z0 = randint(1, 4)
            D = x0**2 + y0**2 + z0**2

            # Hệ số tự do có dạng: mx + ny + pz - D = 0
            # Ở đây ta lấy tỉ lệ k sao cho m, n, p thuộc Z
            k_val = 1
            m = x0 * k_val
            n = y0 * k_val
            p = z0 * k_val
            const_term = D * k_val

            tong = m + n + p
            if -999 < tong < 9999:
                break

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong không gian với trục hệ tọa độ $Oxyz$, cho điểm $H(%s;%s;%s)$ là trực tâm của $\\Delta ABC$ với $A,B,C$ là ba điểm lần lượt nằm trên các trục $Ox,Oy,Oz$ (khác gốc tọa độ). Phương trình mặt phẳng đi qua ba điểm $A,B,C$ có dạng $mx+ny+pz-%s=0$, ($m,n,p \\in \\mathbb{Z}$). Khi đó $m+n+p$ bằng bao nhiêu?'''
                         % (x0, y0, z0, const_term))

        # Nội dung lời giải
        loigiai = ('''Gọi tọa độ các điểm $A(a;0;0)$, $B(0;b;0)$, $C(0;0;c)$ với $a, b, c \\ne 0$.\\\\
    Tứ diện $OABC$ có ba cạnh $OA, OB, OC$ đôi một vuông góc tại gốc tọa độ $O$.\\\\
    Ta chứng minh $OH \\perp (ABC)$:\\\\
    Thật vậy, ta có $\\begin{cases} OA \\perp OB \\\\ OA \\perp OC \\end{cases} \\Rightarrow OA \\perp (OBC) \\Rightarrow OA \\perp BC$.\\\\
    Mặt khác, $H$ là trực tâm tam giác $ABC$ nên $AH \\perp BC$.\\\\
    Từ đó suy ra $BC \\perp (OAH) \\Rightarrow BC \\perp OH$.\\\\
    Chứng minh tương tự, ta cũng có $AB \\perp OH$.\\\\
    Do đó $OH \\perp (ABC)$.\\\\
    Như vậy, mặt phẳng $(ABC)$ nhận vectơ $\\vec{OH} = (%s;%s;%s)$ làm một vectơ pháp tuyến và đi qua điểm $H(%s;%s;%s)$.\\\\
    Phương trình mặt phẳng $(ABC)$ là:\\\\
    $%s(x - %s) + %s(y - %s) + %s(z - %s) = 0$\\\\
    $\\Leftrightarrow %sx + %sy + %sz - (%s) = 0$\\\\
    $\\Leftrightarrow %sx + %sy + %sz - %s = 0$.\\\\
    Đồng nhất phương trình với dạng $mx + ny + pz - %s = 0$, ta được:\\\\
    $m = %s$, $n = %s$, $p = %s$.\\\\
    Vậy $m + n + p = %s + %s + %s = %s$.'''
                   % (x0, y0, z0,
                      x0, y0, z0,
                      x0, x0, y0, y0, z0, z0,
                      x0, y0, z0, x0**2 + y0**2 + z0**2,
                      m, n, p, const_term,
                      const_term,
                      m, n, p,
                      m, n, p, tong))

        # Đáp án
        dapan = '\\shortans{$%s$}\n' % (tong)

    # Xuất câu hỏi với đáp án và lời giải đã được định dạng
    content = ('\\begin{minipage}{\\textwidth}\n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               str(dapan) +
               '\\loigiai{\n' +
               str(loigiai) + '\n}\n' +
               '\\end{ex}\n' +
               '\\end{minipage}\n\n')
    return content

