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


def bt_dang13_p2_b1_c1_ds10(self):
    # Khai báo biến
    # Nội dung câu hỏi
    # Sử dụng biến để có thể dễ dàng thay đổi nội dung nếu cần
    p_text = "Tứ giác $ABCD$ là hình vuông"
    q_text = "Tứ giác $ABCD$ là hình chữ nhật có hai đường chéo vuông góc với nhau"

    noidungcauhoi = ('Cho hai mệnh đề $P$: "%s" và mệnh đề $Q$: "%s". Xét mệnh đề kéo theo "$P \\Rightarrow Q$".' % (p_text, q_text))

    ########################################################################
    # Nhận biết - Câu a: Mệnh đề đảo
    # Mệnh đề đảo của P => Q là Q => P
    da_a_d = '\\True Mệnh đề đảo của mệnh đề "$P \\Rightarrow Q$" là mệnh đề "Nếu $Q$ thì $P$"'
    da_a_s = 'Mệnh đề đảo của mệnh đề "$P \\Rightarrow Q$" là mệnh đề "Nếu $P$ thì $Q$"'
    list_nb_da_1 = [da_a_d, da_a_s]
    nb_da_1 = random.choice(list_nb_da_1)

    loigiai_nb_1 = ('Mệnh đề đảo của mệnh đề "$P \\Rightarrow Q$" được phát biểu là "$Q \\Rightarrow P$". Do đó mệnh đề này là đúng.')

    ########################################################################
    # Thông hiểu - Câu b: Tương đương
    # P <=> Q là đúng
    da_b_d = '\\True Hai mệnh đề $P$ và $Q$ là tương đương với nhau'
    da_b_s = 'Hai mệnh đề $P$ và $Q$ không tương đương với nhau'
    list_th_da_1 = [da_b_d, da_b_s]
    th_da_1 = random.choice(list_th_da_1)

    loigiai_th_1 = ('Vì hình vuông chính là hình chữ nhật có hai đường chéo vuông góc, nên $P \\Rightarrow Q$ và $Q \\Rightarrow P$ đều đúng. Do đó $P$ và $Q$ tương đương với nhau.')

    ########################################################################
    # Vận dụng - Câu c: Xét tính đúng của P <=> Q
    # Mệnh đề này là ĐÚNG
    da_c_d = '\\True Mệnh đề "$P \\Leftrightarrow Q$" là mệnh đề đúng'
    da_c_s = 'Mệnh đề "$P \\Leftrightarrow Q$" là mệnh đề sai'
    list_vd_da_1 = [da_c_d, da_c_s]
    vd_da_1 = random.choice(list_vd_da_1)

    loigiai_vd_1 = ('Vì $P \\Rightarrow Q$ và $Q \\Rightarrow P$ đều là mệnh đề đúng nên mệnh đề "$P \\Leftrightarrow Q$" là mệnh đề đúng.')

    ########################################################################
    # Vận dụng cao - Câu d: Điều kiện cần và đủ
    # P là ĐK cần và đủ của Q
    da_d_d = '\\True $P$ là điều kiện cần và đủ để có $Q$'
    da_d_s = '$P$ chỉ là điều kiện đủ mà không là điều kiện cần để có $Q$'
    list_vdc_da_1 = [da_d_d, da_d_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    loigiai_vdc_1 = ('Vì $P \\Leftrightarrow Q$ là mệnh đề đúng nên $P$ là điều kiện cần và đủ để có $Q$.')

    ########################################################################
    # Logic xử lý
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list để shuffle
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    # Kết hợp
    combined_nb = list(zip(list_nb_1, [loigiai_nb_1]))
    combined_th = list(zip(list_th_1, [loigiai_th_1]))
    combined_vd = list(zip(list_vd_1, [loigiai_vd_1]))
    combined_vdc = list(zip(list_vdc_1, [loigiai_vdc_1]))

    # Xáo trộn
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content

