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


def bt_dang11_p2_b1_c1_hh11(self):
    # Khai báo biến (Random tên các điểm để tạo ra nhiều câu hỏi khác nhau)
    ptM = random.choice(['M', 'E', 'P'])
    ptN = random.choice(['N', 'F', 'Q'])
    ptK = random.choice(['K', 'H', 'R'])

    # Tách riêng hình vẽ thành biến hinhve
    hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]
    \\coordinate (A) at (1,2);
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4,0);
    \\coordinate (D) at (5,2);
    \\coordinate (S) at (2.5,5.5);
    \\coordinate (O) at (intersection of A--C and B--D);
    \\coordinate (N) at ($(B)!0.75!(C)$);
    \\coordinate (K) at (intersection of A--N and C--D);
    \\coordinate (M) at ($(S)!0.4!(C)$);
    \\draw[dashed] (A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O) (A)--(M) (A)--(K) (S)--(A);
    \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(K) (M)--(K) (N)--(K) (C)--(D);
    \\fill (S) circle (1.5pt) node[above] {$S$};
    \\fill (A) circle (1.5pt) node[above left] {$A$};
    \\fill (B) circle (1.5pt) node[below left] {$B$};
    \\fill (C) circle (1.5pt) node[below] {$C$};
    \\fill (D) circle (1.5pt) node[above right] {$D$};
    \\fill (O) circle (1.5pt) node[below] {$O$};
    \\fill (M) circle (1.5pt) node[right] {$%s$};
    \\fill (N) circle (1.5pt) node[below] {$%s$};
    \\fill (K) circle (1.5pt) node[below right] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (ptM, ptN, ptK))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ với $%s$ là một điểm trên cạnh $SC$, $%s$ là một điểm trên cạnh $BC$. Gọi $O = AC \\cap BD$ và $%s = A%s \\cap CD$.'''                  
                     % (ptM, ptN, ptK, ptN))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $SO$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$' 
    nb_da_1_s = '$SD$ là giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$' 
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $S \\in (SAC) \\cap (SBD)$.\\\\
    Lại có $O = AC \\cap BD \\Rightarrow \\begin{cases} O \\in AC \\subset (SAC) \\\\ O \\in BD \\subset (SBD) \\end{cases} \\Rightarrow O \\in (SAC) \\cap (SBD)$.\\\\
    Vậy $(SAC) \\cap (SBD) = SO$.''')

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
    th_da_1_d = '\\True Giao điểm của đường thẳng $A%s$ và mặt phẳng $(SBD)$ là điểm nằm trên cạnh $SO$' % (ptM)
    th_da_1_s = 'Giao điểm của đường thẳng $A%s$ và mặt phẳng $(SBD)$ là điểm nằm trên cạnh $SD$' % (ptM)
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Trong mặt phẳng $(SAC)$, gọi $I = A%s \\cap SO$.\\\\
    Vì $SO \\subset (SBD) \\Rightarrow I \\in (SBD)$.\\\\
    Do đó $I = A%s \\cap (SBD)$.\\\\
    Vậy giao điểm của đường thẳng $A%s$ và mặt phẳng $(SBD)$ là điểm nằm trên cạnh $SO$.'''
               % (ptM, ptM, ptM))

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
    vd_da_1_d = '\\True $%s%s$ là giao tuyến của hai mặt phẳng $(A%s%s)$ và $(SCD)$' % (ptK, ptM, ptM, ptN)
    vd_da_1_s = '$%s%s$ là giao tuyến của hai mặt phẳng $(A%s%s)$ và $(SCD)$' % (ptN, ptM, ptM, ptN)
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có $%s \\in SC \\subset (SCD)$ và $%s \\in (A%s%s) \\Rightarrow %s \\in (A%s%s) \\cap (SCD)$.\\\\
    Lại có $%s = A%s \\cap CD \\Rightarrow \\begin{cases} %s \\in A%s \\subset (A%s%s) \\\\ %s \\in CD \\subset (SCD) \\end{cases} \\Rightarrow %s \\in (A%s%s) \\cap (SCD)$.\\\\
    Vậy $(A%s%s) \\cap (SCD) = %s%s$.'''  
               % (ptM, ptM, ptM, ptN, ptM, ptM, ptN, ptK, ptN, ptK, ptN, ptM, ptN, ptK, ptK, ptM, ptN, ptM, ptN, ptK, ptM))

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
    vdc_da_1_d = '\\True Giao điểm của đường thẳng $SD$ và mặt phẳng $(A%s%s)$ là điểm nằm trên cạnh $%s%s$' % (ptM, ptN, ptK, ptM)
    vdc_da_1_s = 'Giao điểm của đường thẳng $SD$ và mặt phẳng $(A%s%s)$ là điểm nằm trên cạnh $S%s$' % (ptM, ptN, ptM)
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Trong mặt phẳng $(SCD)$, gọi $P = %s%s \\cap SD$.\\\\
    Vì $%s%s \\subset (A%s%s) \\Rightarrow P \\in (A%s%s)$.\\\\
    Do đó $P = SD \\cap (A%s%s)$.\\\\
    Vậy giao điểm của đường thẳng $SD$ và mặt phẳng $(A%s%s)$ là điểm nằm trên cạnh $%s%s$.'''
               % (ptK, ptM, ptK, ptM, ptM, ptN, ptM, ptN, ptM, ptN, ptM, ptN, ptK, ptM))

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

