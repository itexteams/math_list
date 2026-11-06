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


def bt_dang14_p4_b1_c1_ds10(self):
    # Khai báo biến
    # - Đảm bảo cấu trúc đáp án luôn đúng với logic toán học.

    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':
        # Random thông số cho câu a (Mệnh đề chứa biến)
        a_val = random.randint(2, 9)
        b_val = random.randint(1, 10)
        c_val = random.randint(1, 10)
        cau_a = f"{a_val}x + {b_val} > {c_val}"

        # Random thông số cho câu b (Phương trình bậc 2)
        # Chọn hệ số sao cho có thể có nghiệm hoặc vô nghiệm, nhưng bản chất vẫn là mệnh đề
        m = random.randint(1, 5)
        n = random.randint(1, 5)
        cau_b = f"Phương trình $x^2 + {m}x - {n} = 0$ có nghiệm."

        # Random thông số cho câu c (Mệnh đề chứa ký hiệu với mọi)
        p = random.randint(2, 7)
        q = random.randint(1, 5)
        cau_c = f"$\\forall x \\in \\mathbb{{R}}, {p}x > {q}$."

        # Random câu cảm thán cho câu d
        list_cam_than = [
            "Hôm nay thời tiết đẹp quá!",
            "Trời ơi, nóng quá!",
            "Bạn học giỏi quá!",
            "Ôi, bức tranh này tuyệt đẹp!"
        ]
        cau_d = random.choice(list_cam_than)

        # Nội dung câu hỏi
        noidungcauhoi = (f"Trong các câu sau, tìm các câu là mệnh đề.\\\\ \n"
                            f"a) ${cau_a}$.\\\\ \n"
                            f"b) {cau_b}\\\\ \n"
                            f"c) {cau_c}\\\\\n"
                            f"d) {cau_d}")

        # Đáp án đúng luôn là 2 (câu b và c)
        da_d = "\\True 2"

        # Các đáp án sai
        s = ["1", "3", "4", "0"]
        random.shuffle(s)
        da_s1 = s[0]
        da_s2 = s[1]
        da_s3 = s[2]

        # Trộn đáp án
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)

        # Lời giải
        loigiai = (f"Các câu là mệnh đề bao gồm:\\\\ \n"
                    f"- Câu b: \"{cau_b}\" là một khẳng định có tính đúng sai khách quan.\\\\ \n"
                    f"- Câu c: \"{cau_c}\" là một mệnh đề toán học.\\\\ \n"
                    f"Câu a là mệnh đề chứa biến, câu d là câu cảm thán nên không phải là mệnh đề.")

    # B2: Xuất câu trắc nghiệm theo mẫu
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

