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


def bt_dang33_p1_b1_c5_ds11(self):
            # Khai báo biến
            # Ta chọn n2 và hệ số k để n1 = n2 * k (giống cấu trúc đề bài n1=21, n2=7, k=3)
            n2 = random.choice([3, 5, 7, 11])
            k = random.randint(2, 4)
            n1 = n2 * k

            # Chọn m1 và m2 sao cho m1 và k*m2 không quá lớn và không bằng nhau
            m2 = random.randint(1, 5)
            # Để tạo ra trường hợp 0 < a < 1, ta cần m1 < k*m2
            # Để tạo ra trường hợp a > 1, ta cần m1 > k*m2
            case = random.choice(['0<a<1', 'a>1'])

            if case == '0<a<1':
                m1 = random.randint(1, k * m2 - 1)
            else:
                m1 = random.randint(k * m2 + 1, k * m2 + 5)

            m2_new = m2 * k # Số mũ sau khi quy đồng

            # --- Thiết lập nội dung ---

            # Câu hỏi
            noidungcauhoi = r"Giá trị của $a$ để $\sqrt[%s]{a^{%s}} > \sqrt[%s]{a^{%s}}$ là" % (latex(n1), latex(m1), latex(n2), latex(m2))

            # Đáp án đúng
            da_dung = r"$0 < a < 1$" if case == '0<a<1' else r"$a > 1$"
            da_sai1 = r"$a > 1$" if case == '0<a<1' else r"$0 < a < 1$"
            da_sai2 = r"$a > 0$"
            da_sai3 = r"$a \in \mathbb{R}$"

            # Trộn đáp án
            list_da = [r"\True " + da_dung, da_sai1, da_sai2, da_sai3]
            random.shuffle(list_da)

            # Lời giải chi tiết
            loigiai = r"""Ta có $\sqrt[%s]{a^{%s}} = \sqrt[%s \cdot %s]{a^{%s \cdot %s}} = \sqrt[%s]{a^{%s}}$. \\
            Khi đó bất phương trình trở thành: $\sqrt[%s]{a^{%s}} > \sqrt[%s]{a^{%s}}$. \\
            Vì $%s %s %s$ nên để bất đẳng thức trên đúng thì $%s$.""" % (
                latex(n2), latex(m2), latex(n2), latex(k), latex(m2), latex(k), latex(n1), latex(m2_new),
                latex(n1), latex(m1), latex(n1), latex(m2_new),
                latex(m1), "<" if m1 < m2_new else ">", latex(m2_new),
                da_dung.replace("$", "")
            )

            # Xuất kết quả theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_da[0])+'}\n'
                '{'+str(list_da[1])+'}\n'
                '{'+str(list_da[2])+'}\n'
                '{'+str(list_da[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

