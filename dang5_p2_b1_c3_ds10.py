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


def bt_dang5_p2_b1_c3_ds10(self):
    # Khai báo biến
    vat_do = random.choice(['một chiếc bàn', 'một cây thước', 'một sợi dây', 'một phòng học'])
    don_vi_dem = random.choice(['một lớp', 'một hội trường', 'một xe buýt'])
    
    # Nội dung câu hỏi
    noidungcauhoi = ('''Xét các phát biểu về số đúng và số gần đúng.'''
                     )
    
    ######################################## Ý a ########################################
    # Ý a: Kết quả đo đạc thường là số gần đúng (Đúng) / số đúng (Sai)
    a_dung_text = 'Kết quả đo chiều dài %s thường là một số gần đúng' % vat_do
    a_sai_text = 'Kết quả đo chiều dài %s luôn luôn là một số đúng' % vat_do
    
    a_da_d = '\\True ' + a_dung_text
    a_da_s = a_sai_text
    list_nb_da_1 = [a_da_d, a_da_s]
    
    loigiai_a_d = ('''Kết quả đo chiều dài %s phụ thuộc vào dụng cụ đo và sai số thực tế nên thường là một số gần đúng.''' % vat_do)
    loigiai_a_s = ('''Kết quả đo đạc phụ thuộc vào độ chính xác của dụng cụ và thao tác đo nên thường chỉ là số gần đúng, không thể luôn là số đúng.''' )
    
    list_a_lg = [loigiai_a_d, loigiai_a_s]
    
    ######################################## Ý b ########################################
    # Ý b: Đếm số lượng cụ thể tại một thời điểm có thể là số đúng (Đúng) / luôn là số gần đúng (Sai)
    b_dung_text = 'Số học sinh có mặt trong %s tại một thời điểm, nếu đếm đầy đủ, có thể là số đúng' % don_vi_dem
    b_sai_text = 'Số học sinh có mặt trong %s tại một thời điểm, dù đếm trực tiếp, luôn là số gần đúng' % don_vi_dem
    
    b_da_d = '\\True ' + b_dung_text
    b_da_s = b_sai_text
    list_th_da_1 = [b_da_d, b_da_s]
    
    loigiai_b_d = ('''Số lượng phần tử rời rạc xác định qua phép đếm cẩn thận, đầy đủ có thể xác định chính xác số đúng.''' )
    loigiai_b_s = ('''Số học sinh có mặt tại một thời điểm hoàn toàn có thể xác định chính xác bằng phép đếm, nên không bắt buộc luôn là số gần đúng.''' )
    
    list_b_lg = [loigiai_b_d, loigiai_b_s]
    
    ######################################## Ý c ########################################
    # Ý c: Mọi số nguyên đều là số đúng trong mọi tình huống (Sai) / Số nguyên cũng có thể là số gần đúng trong một số tình huống (Đúng)
    c_dung_text = 'Một số nguyên vẫn có thể là số gần đúng trong các bài toán đo đạc hoặc ước lượng'
    c_sai_text = 'Mọi số nguyên đều là số đúng trong mọi tình huống'
    
    c_da_d = '\\True ' + c_dung_text
    c_da_s = c_sai_text
    list_vd_da_1 = [c_da_s, c_da_d]  # c_sai_text tương ứng khẳng định c gốc là Sai
    
    loigiai_c_s = ('''Trong nhiều trường hợp đo đạc hoặc ước lượng, người ta làm tròn đến hàng đơn vị, chục, trăm nên số nguyên nhận được vẫn là số gần đúng.''' )
    loigiai_c_d = ('''Số nguyên thu được từ việc làm tròn số đo hoặc ước lượng là số gần đúng.''' )
    
    list_c_lg = [loigiai_c_s, loigiai_c_d]
    
    ######################################## Ý d ########################################
    # Ý d: Khái niệm sử dụng số gần đúng thay cho số đúng khi số đúng khó biết
    d_dung_text = 'Một số gần đúng có thể được dùng thay cho số đúng khi số đúng khó xác định chính xác'
    d_sai_text = 'Không bao giờ được dùng số gần đúng thay cho số đúng'
    
    d_da_d = '\\True ' + d_dung_text
    d_da_s = d_sai_text
    list_vdc_da_1 = [d_da_d, d_da_s]
    
    loigiai_d_d = ('''Khi số đúng khó hoặc chưa thể biết chính xác, ta sử dụng số gần đúng để tính toán và mô tả đại lượng.''' )
    loigiai_d_s = ('''Trong thực tế, khi không thể biết số đúng thì số gần đúng là giá trị được dùng để thay thế.''' )
    
    list_d_lg = [loigiai_d_d, loigiai_d_s]
    
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    
    # Lặp chọn để đảm bảo có từ 1 đến 3 khẳng định đúng
    while True:
        idx_a = random.choice([0, 1])
        idx_b = random.choice([0, 1])
        idx_c = random.choice([0, 1])
        idx_d = random.choice([0, 1])
        
        nb_da_1 = list_nb_da_1[idx_a]
        loigiai_nb_1 = list_a_lg[idx_a]
        
        th_da_1 = list_th_da_1[idx_b]
        loigiai_th_1 = list_b_lg[idx_b]
        
        vd_da_1 = list_vd_da_1[idx_c]
        loigiai_vd_1 = list_c_lg[idx_c]
        
        vdc_da_1 = list_vdc_da_1[idx_d]
        loigiai_vdc_1 = list_d_lg[idx_d]
        
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break
    
    # Gán vào danh sách
    shuffled_answers_nb = [nb_da_1]
    shuffled_solutions_nb = [loigiai_nb_1]
    
    shuffled_answers_th = [th_da_1]
    shuffled_solutions_th = [loigiai_th_1]
    
    shuffled_answers_vd = [vd_da_1]
    shuffled_solutions_vd = [loigiai_vd_1]
    
    shuffled_answers_vdc = [vdc_da_1]
    shuffled_solutions_vdc = [loigiai_vdc_1]
    
    # Xuất câu hỏi theo định dạng Đúng/Sai (choiceTF)
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTF \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{itemchoice} \n'
               '\\itemch ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\itemch ' + str(shuffled_solutions_th[0]) + '\n'
               '\\itemch ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\itemch ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{itemchoice}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
    