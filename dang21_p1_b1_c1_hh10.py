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


def bt_dang21_p1_b1_c1_hh10(self):
            # Khai báo biến
            # B3: Suy nghĩ cách random
            # Khai báo bộ dữ liệu cho các trường hợp góc nhọn trong tam giác vuông ABC (vuông tại A)
            data_tam_giac = [
                {
                    "goc_ten": "B",
                    "goc_val": "30^\\circ",
                    "trues": [
                        "\\sin B = \\frac{1}{2}",
                        "\\cos B = \\frac{\\sqrt{3}}{2}",
                        "\\tan B = \\frac{\\sqrt{3}}{3}",
                        "\\cot B = \\sqrt{3}",
                        "\\sin C = \\frac{\\sqrt{3}}{2}",
                        "\\cos C = \\frac{1}{2}",
                        "\\tan C = \\sqrt{3}",
                        "\\cot C = \\frac{\\sqrt{3}}{3}"
                    ],
                    "falses": [
                        {"stmt": "\\cos B = \\frac{1}{\\sqrt{3}}", "expl": "\\cos B = \\cos 30^\\circ = \\frac{\\sqrt{3}}{2}"},
                        {"stmt": "\\sin B = \\frac{\\sqrt{3}}{2}", "expl": "\\sin B = \\sin 30^\\circ = \\frac{1}{2}"},
                        {"stmt": "\\sin C = \\frac{1}{2}", "expl": "\\widehat{C} = 90^\\circ - 30^\\circ = 60^\\circ \\Rightarrow \\sin C = \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}"},
                        {"stmt": "\\cos C = \\frac{\\sqrt{3}}{2}", "expl": "\\widehat{C} = 90^\\circ - 30^\\circ = 60^\\circ \\Rightarrow \\cos C = \\cos 60^\\circ = \\frac{1}{2}"}
                    ]
                },
                {
                    "goc_ten": "B",
                    "goc_val": "60^\\circ",
                    "trues": [
                        "\\sin B = \\frac{\\sqrt{3}}{2}",
                        "\\cos B = \\frac{1}{2}",
                        "\\tan B = \\sqrt{3}",
                        "\\cot B = \\frac{\\sqrt{3}}{3}",
                        "\\sin C = \\frac{1}{2}",
                        "\\cos C = \\frac{\\sqrt{3}}{2}",
                        "\\tan C = \\frac{\\sqrt{3}}{3}",
                        "\\cot C = \\sqrt{3}"
                    ],
                    "falses": [
                        {"stmt": "\\cos B = \\frac{\\sqrt{3}}{2}", "expl": "\\cos B = \\cos 60^\\circ = \\frac{1}{2}"},
                        {"stmt": "\\sin B = \\frac{1}{2}", "expl": "\\sin B = \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}"},
                        {"stmt": "\\sin C = \\frac{\\sqrt{3}}{2}", "expl": "\\widehat{C} = 90^\\circ - 60^\\circ = 30^\\circ \\Rightarrow \\sin C = \\sin 30^\\circ = \\frac{1}{2}"},
                        {"stmt": "\\cos C = \\frac{1}{2}", "expl": "\\widehat{C} = 90^\\circ - 60^\\circ = 30^\\circ \\Rightarrow \\cos C = \\cos 30^\\circ = \\frac{\\sqrt{3}}{2}"}
                    ]
                },
                {
                    "goc_ten": "C",
                    "goc_val": "30^\\circ",
                    "trues": [
                        "\\sin C = \\frac{1}{2}",
                        "\\cos C = \\frac{\\sqrt{3}}{2}",
                        "\\tan C = \\frac{\\sqrt{3}}{3}",
                        "\\cot C = \\sqrt{3}",
                        "\\sin B = \\frac{\\sqrt{3}}{2}",
                        "\\cos B = \\frac{1}{2}",
                        "\\tan B = \\sqrt{3}",
                        "\\cot B = \\frac{\\sqrt{3}}{3}"
                    ],
                    "falses": [
                        {"stmt": "\\cos C = \\frac{1}{\\sqrt{3}}", "expl": "\\cos C = \\cos 30^\\circ = \\frac{\\sqrt{3}}{2}"},
                        {"stmt": "\\sin C = \\frac{\\sqrt{3}}{2}", "expl": "\\sin C = \\sin 30^\\circ = \\frac{1}{2}"},
                        {"stmt": "\\sin B = \\frac{1}{2}", "expl": "\\widehat{B} = 90^\\circ - 30^\\circ = 60^\\circ \\Rightarrow \\sin B = \\sin 60^\\circ = \\frac{\\sqrt{3}}{2}"},
                        {"stmt": "\\cos B = \\frac{\\sqrt{3}}{2}", "expl": "\\widehat{B} = 90^\\circ - 30^\\circ = 60^\\circ \\Rightarrow \\cos B = \\cos 60^\\circ = \\frac{1}{2}"}
                    ]
                }
            ]

            # Lựa chọn ngẫu nhiên 1 trường hợp bài toán
            bai_toan = random.choice(data_tam_giac)

            # Chọn ngẫu nhiên 1 mệnh đề SAI (đáp án đúng của câu hỏi) và 3 mệnh đề ĐÚNG (phương án nhiễu)
            da_sai_dict = random.choice(bai_toan["falses"])
            da_dung_list = random.sample(bai_toan["trues"], 3)

            # B2: Viết lại đề bài và lời giải
            # Câu hỏi
            noidungcauhoi = f"Cho $\\Delta ABC$ vuông tại $A$, góc ${bai_toan['goc_ten']}$ bằng ${bai_toan['goc_val']}$. Khẳng định nào sau đây là \\textbf{{sai}}?"

            # Các đáp án
            da_d = '\\True $' + da_sai_dict["stmt"] + '$'
            da_s1 = '$' + da_dung_list[0] + '$'
            da_s2 = '$' + da_dung_list[1] + '$'
            da_s3 = '$' + da_dung_list[2] + '$'

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Lời giải
            loigiai = f"${da_sai_dict['expl']}$."

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\n\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

