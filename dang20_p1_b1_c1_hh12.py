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


def bt_dang20_p1_b1_c1_hh12(self):
            # Khai báo biến
            # Định nghĩa các loại bài toán
            # Mỗi loại bài toán là một dictionary chứa nội dung câu hỏi, đáp án đúng, đáp án sai và lời giải
            dang_toan_1 = {
                'noidungcauhoi': '''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Mệnh đề nào sau đây đúng?''',
                'dap_an_dung': '$\\vec{SA} + \\vec{SB} + \\vec{SC} + \\vec{SD} = 4\\vec{SO}$',
                'dap_an_sai': [
                        '$\\vec{SA} + \\vec{SB} + \\vec{SC} + \\vec{SD} = 2\\vec{SO}$',
                        '$\\vec{SA} + \\vec{SB} + \\vec{SC} + \\vec{SD} = 3\\vec{SO}$',
                        '$\\vec{SA} + \\vec{SB} + \\vec{SC} + \\vec{SD} = \\vec{0}$',
                        '$\\vec{SA} + \\vec{SB} + \\vec{SC} + \\vec{SD} = 4\\vec{OS}$',
                        '$\\vec{SA} + \\vec{SC} = \\vec{SB} + \\vec{SD}$',
                        '$\\vec{SA} - \\vec{SC} = 2\\vec{SO}$'
                ],
                'loigiai': '''Ta có $O$ là trung điểm của $AC$ và $BD$ nên:\\\\
                    $\\vec{SA} + \\vec{SC} = 2\\vec{SO}$ (theo quy tắc trung điểm) (1)\\\\
                    $\\vec{SB} + \\vec{SD} = 2\\vec{SO}$ (theo quy tắc trung điểm) (2)\\\\
                    Từ (1) và (2) suy ra $\\vec{SA} + \\vec{SB} + \\vec{SC} + \\vec{SD} = 2\\vec{SO} + 2\\vec{SO} = 4\\vec{SO}$.'''
            }

            dang_toan_2 = {
                'noidungcauhoi': '''Cho hình bình hành $ABCD$ có tâm $O$. Mệnh đề nào sau đây đúng?''',
                'dap_an_dung': '$\\vec{AB} + \\vec{AD} = \\vec{AC}$',
                'dap_an_sai': [
                    '$\\vec{AC} = \\vec{AB} - \\vec{AD}$',
                    '$\\vec{AC} = \\vec{BC} - \\vec{DC}$',
                    '$\\vec{AB} + \\vec{CD} = \\vec{AC}$',
                    '$\\vec{DA} + \\vec{DC} = \\vec{AC}$',
                    '$\\vec{AB} + \\vec{AD} = \\vec{CB}$'
                ],
                'loigiai': '''Theo quy tắc hình bình hành, tổng hai vectơ có chung gốc là hai cạnh của hình bình hành bằng vectơ đường chéo.\\\\
                    $\\vec{AB} + \\vec{AD} = \\vec{AC}$.'''
            }

            dang_toan_3 = {
                'noidungcauhoi': '''Cho hình chóp $S.ABC$ có $G$ là trọng tâm tam giác $ABC$. Mệnh đề nào sau đây đúng?''',
                'dap_an_dung': '$\\vec{SA} + \\vec{SB} + \\vec{SC} = 3\\vec{SG}$',
                'dap_an_sai': [
                    '$\\vec{SA} + \\vec{SB} + \\vec{SC} = \\vec{0}$',
                    '$\\vec{SA} + \\vec{SB} + \\vec{SC} = 2\\vec{SG}$',
                    '$\\vec{SA} + \\vec{SB} + \\vec{SC} = 3\\vec{GS}$',
                    '$\\vec{SG} = \\vec{SA} + \\vec{SB} + \\vec{SC}$',
                    '$\\vec{GA} + \\vec{GB} + \\vec{GC} = 3\\vec{SG}$'
                ],
                'loigiai': '''Ta có $G$ là trọng tâm tam giác $ABC$, nên:\\\\
                    $\\vec{GA} + \\vec{GB} + \\vec{GC} = \\vec{0}$.\\\\
                    Áp dụng quy tắc chèn điểm $S$:\\\\
                    $(\\vec{SA} - \\vec{SG}) + (\\vec{SB} - \\vec{SG}) + (\\vec{SC} - \\vec{SG}) = \\vec{0}$.\\\\
                    $\\vec{SA} + \\vec{SB} + \\vec{SC} - 3\\vec{SG} = \\vec{0}$.\\\\
                    $\\vec{SA} + \\vec{SB} + \\vec{SC} = 3\\vec{SG}$.'''
            }

            # Chọn ngẫu nhiên một trong các loại bài toán
            list_dang_toan = [dang_toan_1, dang_toan_2, dang_toan_3]
            dang_toan = random.choice(list_dang_toan)

            # Lấy thông tin từ loại bài toán đã chọn
            noidungcauhoi = dang_toan['noidungcauhoi']
            dap_an_dung = dang_toan['dap_an_dung']
            loigiai = dang_toan['loigiai']

            # Trộn lẫn đáp án
            list_dap_an = [dap_an_dung] + random.sample(dang_toan['dap_an_sai'], 3)
            random.shuffle(list_dap_an)

            # Thêm định dạng đúng/sai
            dap_an_dung_index = list_dap_an.index(dap_an_dung)
            list_dap_an[dap_an_dung_index] = '\\True ' + list_dap_an[dap_an_dung_index]

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + noidungcauhoi +
                '\\choice \n'
                '{' + list_dap_an[0] + '}\n'
                '{' + list_dap_an[1] + '}\n'
                '{' + list_dap_an[2] + '}\n'
                '{' + list_dap_an[3] + '}\n'
                '\\loigiai{' + loigiai + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n' )
            return content

