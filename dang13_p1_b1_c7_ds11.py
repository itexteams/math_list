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


def bt_dang13_p1_b1_c7_ds11(self):
            # Khai báo biến
            # B2 & B3: Viết mã Python và thiết kế Random
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random tên biến số để bài toán phong phú
                # Biến chính, điểm đang xét, số gia
                vars_list = [
                    {'x': 'x', 'x0': 'x_0', 'delta': '\\Delta x', 'h': 'h'},
                    {'x': 't', 'x0': 't_0', 'delta': '\\Delta t', 'h': 'k'},
                    {'x': 'u', 'x0': 'u_0', 'delta': '\\Delta u', 'h': 's'}
                ]
                v = random.choice(vars_list)
                x = v['x']
                x0 = v['x0']
                dx = v['delta']
                h = v['h']

                # Nội dung câu hỏi
                noidungcauhoi = (f"Cho hàm số $y = f(x)$ có đạo hàm tại ${x0}$ là $f'({x0})$. Khẳng định nào sau đây là \\textbf{{sai}}?")

                # Các đáp án
                # Đáp án A (Sai - Theo đề bài gốc)
                da_sai = f"$f'({x0}) = \\lim_{{{x} \\to {x0}}} \\frac{{f({x} + {x0}) - f({x0})}}{{{x} - {x0}}}$"

                # Các đáp án đúng
                da_dung1 = f"$f'({x0}) = \\lim_{{{dx} \\to 0}} \\frac{{f({x0} + {dx}) - f({x0})}}{{{dx}}}$"
                da_dung2 = f"$f'({x0}) = \\lim_{{{x} \\to {x0}}} \\frac{{f({x}) - f({x0})}}{{{x} - {x0}}}$"
                da_dung3 = f"$f'({x0}) = \\lim_{{{h} \\to 0}} \\frac{{f({h} + {x0}) - f({x0})}}{{{h}}}$"

                # Gán nhãn \True cho đáp án sai (vì đề bài hỏi khẳng định SAI)
                da_d = '\\True ' + da_sai
                da_s1 = da_dung1
                da_s2 = da_dung2
                da_s3 = da_dung3

                # Trộn đáp án
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải
                loigiai = (f"Theo định nghĩa đạo hàm của hàm số tại một điểm ${x0}$:\n"
                           f"$$f'({x0}) = \\lim_{{{x} \\to {x0}}} \\frac{{f({x}) - f({x0})}}{{{x} - {x0}}}$$ "
                           f"hoặc $$f'({x0}) = \\lim_{{{dx} \\to 0}} \\frac{{f({x0} + {dx}) - f({x0})}}{{{dx}}}.$$\n"
                           f"Do đó, khẳng định $f'({x0}) = \\lim_{{{x} \\to {x0}}} \\frac{{f({x} + {x0}) - f({x0})}}{{{x} - {x0}}}$ là khẳng định sai.")

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

