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


def bt_dang7_p2_b1_c1_hh11(self):
    # Khai báo biến (Random tên các điểm để tạo ra nhiều đề khác nhau)
    ptE = random.choice(['E', 'M', 'P'])
    ptF = random.choice(['F', 'N', 'Q'])
    ptG = random.choice(['G', 'H', 'K'])

    # Tách riêng hình vẽ thành biến hinhve
    hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.9, line join=round, line cap=round, line width=1pt]
    \\coordinate (D) at (0,0);
    \\coordinate (C) at (6,0);
    \\coordinate (B) at (4,1.5);
    \\coordinate (A) at (1,2);
    \\coordinate (S) at (2,5);
    \\coordinate (E) at (intersection of A--B and D--C);
    \\coordinate (F) at (intersection of A--C and B--D);
    \\coordinate (G) at (intersection of E--F and A--D);
    \\draw[dashed] (A)--(D) (A)--(B) (S)--(B) (S)--(A) (A)--(C) (B)--(D) (F)--(G) (S)--(F) (S)--(G) (B)--(C) (B)--(E) (E)--(F);
    \\draw (S)--(D) (S)--(C)  (D)--(C) (C)--(E)  (S)--(E);
    \\fill (S) circle (1.5pt) node[above] {$S$};
    \\fill (A) circle (1.5pt) node[left] {$A$};
    \\fill (B) circle (1.5pt) node[above right] {$B$};
    \\fill (C) circle (1.5pt) node[below right] {$C$};
    \\fill (D) circle (1.5pt) node[below left] {$D$};
    \\fill (E) circle (1.5pt) node[right] {$%s$};
    \\fill (F) circle (1.5pt) node[below] {$%s$};
    \\fill (G) circle (1.5pt) node[left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (ptE, ptF, ptG))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$, biết $AB$ cắt $CD$ tại $%s$, $AC$ cắt $BD$ tại $%s$ trong mặt phẳng đáy.'''                  
                     % (ptE, ptF))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Đường thẳng $%s%s$ nằm trong mặt phẳng $(ABCD)$' % (ptE, ptF)
    nb_da_1_s = 'Đường thẳng $%s%s$ nằm trong mặt phẳng $(SAB)$' % (ptE, ptF)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Vì $%s \\in CD \\subset (ABCD)$ và $%s \\in BD \\subset (ABCD)$ nên đường thẳng $%s%s$ nằm trong mặt phẳng $(ABCD)$.'''
                % (ptE, ptF, ptE, ptF))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True $AB$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(ABCD)$' 
    th_da_1_s = '$AC$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(ABCD)$' 
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Ta có $A, B$ là hai điểm chung của mặt phẳng $(SAB)$ và $(ABCD)$.\\\\
    Do đó $(SAB) \\cap (ABCD) = AB$.''')

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## 
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True $S%s$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$, $S%s$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$' % (ptE, ptF)
    vd_da_1_s = '$S%s$ là giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$, $S%s$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$' % (ptF, ptE)
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có $S$ là điểm chung của $(SAB)$ và $(SCD)$. \\\\
    Lại có $%s = AB \\cap CD \\Rightarrow \\begin{cases} %s \\in AB \\subset (SAB) \\\\ %s \\in CD \\subset (SCD) \\end{cases} \\Rightarrow %s \\in (SAB) \\cap (SCD)$. \\\\
    Suy ra $(SAB) \\cap (SCD) = S%s$. \\\\
    Tương tự, $S$ là điểm chung của $(SAC)$ và $(SBD)$. \\\\
    $%s = AC \\cap BD \\Rightarrow \\begin{cases} %s \\in AC \\subset (SAC) \\\\ %s \\in BD \\subset (SBD) \\end{cases} \\Rightarrow %s \\in (SAC) \\cap (SBD)$. \\\\
    Suy ra $(SAC) \\cap (SBD) = S%s$.'''  
               % (ptE, ptE, ptE, ptE, ptE, ptF, ptF, ptF, ptF, ptF))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## 
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Gọi $%s = %s%s \\cap AD$ khi đó, $S%s$ là giao tuyến của mặt phẳng $(S%s%s)$ và mặt phẳng $(SAD)$' % (ptG, ptE, ptF, ptG, ptE, ptF)
    vdc_da_1_s = 'Gọi $%s = %s%s \\cap AD$ khi đó, $S%s$ là giao tuyến của mặt phẳng $(S%s%s)$ và mặt phẳng $(SCD)$' % (ptG, ptE, ptF, ptG, ptE, ptF)
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Điểm $S$ là điểm chung của mặt phẳng $(S%s%s)$ và $(SAD)$. \\\\
    Lại có $%s = %s%s \\cap AD \\Rightarrow \\begin{cases} %s \\in %s%s \\subset (S%s%s) \\\\ %s \\in AD \\subset (SAD) \\end{cases} \\Rightarrow %s \\in (S%s%s) \\cap (SAD)$. \\\\
    Vậy giao tuyến của $(S%s%s)$ và $(SAD)$ là $S%s$.'''
               % (ptE, ptF, ptG, ptE, ptF, ptG, ptE, ptF, ptE, ptF, ptG, ptG, ptE, ptF, ptE, ptF, ptG))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

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

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    # Gọi biến hinhve ở đầu phần loigiai
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
       '{'+str(shuffled_answers_nb[0])+'}\n'
       '{'+str(shuffled_answers_th[0])+'}\n'
       '{'+str(shuffled_answers_vd[0])+'}\n'
       '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        + str(hinhve) + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

