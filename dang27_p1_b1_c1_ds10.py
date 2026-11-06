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


def bt_dang27_p1_b1_c1_ds10(self):
    # Khai báo biến
    # Mệnh đề I: Thay đổi số chia hết để mệnh đề đảo có thể Đúng hoặc Sai
    n1 = random.choice([10, 12, 14, 18, 20])
    n2 = n1 // 2
    is_prop1_dao_dung = random.choice([True, False])
    if is_prop1_dao_dung:
        text_prop1 = f"Mệnh đề “Nếu một số chia hết cho {n2} thì số ấy chia hết cho {n1}” có mệnh đề đảo là mệnh đề đúng.\\\\"
        prop1_is_false = False
        prop1_solve = f"Mệnh đề đảo là “Nếu một số chia hết cho {n1} thì số ấy chia hết cho {n2}”, đây là mệnh đề đúng.\\\\"
    else:
        text_prop1 = f"Mệnh đề “Nếu một số chia hết cho {n1} thì số ấy chia hết cho {n2}” có mệnh đề đảo là mệnh đề đúng.\\\\"
        prop1_is_false = True
        prop1_solve = f"Mệnh đề đảo là “Nếu một số chia hết cho {n2} thì số ấy chia hết cho {n1}”, đây là mệnh đề sai (ví dụ {n2} không chia hết cho {n1}).\\\\"

    # Mệnh đề III: Random giữa các mệnh đề Sai và Đúng
    list_prop3 = [
        (r"\exists x \in \mathbb{N}, x > x^2", True, r"$x > x^2 \Leftrightarrow 0 < x < 1$, không có số tự nhiên nào thỏa mãn."),
        (r"\exists x \in \mathbb{R}, x^2 < 0", True, r"Bình phương của một số thực luôn không âm."),
        (r"\exists x \in \mathbb{Z}, x^2 = x", False, r"Với $x=1$ thì $1^2=1$, đây là mệnh đề đúng.")
    ]
    prop3_text, prop3_is_false, prop3_explain = random.choice(list_prop3)

    # Mệnh đề IV: Random tính chẵn lẻ
    list_prop4 = [
        (r"\forall n \in \mathbb{N}, n^2 + n \text{ là số lẻ}", True, r"$n(n+1)$ là tích hai số liên tiếp nên phải là số chẵn."),
        (r"\forall n \in \mathbb{N}, n^2 + n \text{ là số chẵn}", False, r"$n(n+1)$ luôn là số chẵn, đây là mệnh đề đúng.")
    ]
    prop4_text, prop4_is_false, prop4_explain = random.choice(list_prop4)

    # --- TỔNG HỢP DANH SÁCH MỆNH ĐỀ ---
    propositions = [
        {"id": "I", "text": text_prop1, "is_false": prop1_is_false, "solve": prop1_solve},
        {"id": "II", "text": "Mệnh đề $P$: “Có ít nhất một số vô tỷ là số thập phân vô hạn tuần hoàn” có mệnh đề phủ định $\\overline{P}$ là mệnh đề đúng.\\\\", "is_false": False, "solve": "Vì $P$ sai nên $\\overline{P}$ đúng. Phát biểu này ĐÚNG."},
        {"id": "III", "text": f"${prop3_text}$.\\\\", "is_false": prop3_is_false, "solve": f"Mệnh đề này SAI vì {prop3_explain}" if prop3_is_false else f"Mệnh đề này ĐÚNG vì {prop3_explain}"},
        {"id": "IV", "text": f"${prop4_text}$.\\\\", "is_false": prop4_is_false, "solve": f"Mệnh đề này SAI vì {prop4_explain}" if prop4_is_false else f"Mệnh đề này ĐÚNG vì {prop4_explain}"},
        {"id": "V", "text": "Mệnh đề “Phương trình $x^2 + 1 = 0$ có hai nghiệm phân biệt” là mệnh đề toán học.\\\\", "is_false": False, "solve": "Đây là một khẳng định có tính đúng sai rõ ràng nên là mệnh đề toán học. Phát biểu ĐÚNG."},
        {"id": "VI", "text": "Mệnh đề chứa biến là một mệnh đề.", "is_false": True, "solve": "Theo định nghĩa, mệnh đề chứa biến chưa phải là mệnh đề. Phát biểu này SAI."}
    ]

    # Đếm số mệnh đề sai thực tế sau khi random
    count_false = sum(1 for p in propositions if p['is_false'])

    # --- TẠO NỘI DUNG ---
    noidungcauhoi = "Trong các mệnh đề sau, có bao nhiêu mệnh đề là mệnh đề sai?"
    for p in propositions:
        noidungcauhoi += f"\\textbf{{{p['id']}.}} {p['text']}"

    da_dung = f"\\True {count_false}"
    # Tạo bộ đáp án nhiễu không trùng đáp án đúng
    choices = {0, 1, 2, 3, 4, 5}
    choices.discard(count_false)
    others = random.sample(list(choices), 3)

    list_1 = [da_dung, str(others[0]), str(others[1]), str(others[2])]
    random.shuffle(list_1)

    loigiai = ""
    for p in propositions:
        status = "SAI" if p['is_false'] else "ĐÚNG"
        loigiai += f"\\textbf{{Mệnh đề {p['id']}:}} {p['solve']} $\\Rightarrow$ {status}.\\\\\n"
    loigiai += f"\\textbf{{Kết luận:}} Có {count_false} mệnh đề sai."

    # --- XUẤT CÂU TRẮC NGHIỆM ---
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ 
        '\n \\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-').replace('10x','10 x').replace('+0x','').replace('-0x','').replace('11x','11 x').replace('1x','x').replace('10y','10 y').replace('+0y','').replace('-0y','').replace('11y','11 y').replace('1y','y').replace('10t','10 t').replace('+0t','').replace('-0t','').replace('11t','11 t').replace('1t','t')
    return content

