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


def bt_dang4_p2_b4_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        # Hình vẽ TikZ theo đúng mẫu ảnh và phong cách yêu cầu
        tikz_fig = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.7, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (1.8,-1.8);
    \\coordinate (C) at (7,0);
    \\coordinate (A1) at (1.5,6.5);
    \\coordinate (B1) at ($(B)+(A1)-(A)$);
    \\coordinate (C1) at ($(C)+(A1)-(A)$);
    \\coordinate (M) at ($(B)!0.5!(C)$);
    \\coordinate (M1) at ($(B1)!0.5!(C1)$);
    \\coordinate (N) at ($(C)!0.5!(C1)$);
    \\coordinate (I) at ($(A)!0.66667!(M)$);
    \\coordinate (K) at ($(A1)!0.66667!(M1)$);
    \\coordinate (G) at ($(A)!0.66667!(N)$);
    \\draw[line width=1pt] (A)--(B)--(C) (A1)--(B1)--(C1)--(A1) (A)--(A1) (B)--(B1) (C)--(C1) (A1)--(K)--(M1) (M)--(N);
    \\draw[line width=1pt, dashed] (A)--(C) (A)--(M) (A)--(N) (I)--(K)--(G)--(I) (A1)--(C);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (A1) circle (1pt) node[above left] {$A'$};
    \\fill (B1) circle (1pt) node[left] {$B'$};
    \\fill (C1) circle (1pt) node[above right] {$C'$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\fill (M1) circle (1pt) node[above] {$M'$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (I) circle (1pt) node[below left] {$I$};
    \\fill (K) circle (1pt) node[above] {$K$};
    \\fill (G) circle (1pt) node[right] {$G$};
\\end{tikzpicture}
\\end{center}''')
        
        # Khai báo biến và tạo ngẫu nhiên tỉ số sai
        wrong_ratio = random.choice(["\\frac{1}{3}", "\\frac{1}{2}", "\\frac{3}{4}"])
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho lăng trụ tam giác $ABC.A'B'C'$ có $I, K, G$ lần lượt là trọng tâm các tam giác $ABC, A'B'C', ACC'$. Gọi $M, M'$ lần lượt là trung điểm của $BC, B'C'$.''')
        
        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True $AMM\'A\'$ là hình bình hành'
        nb_da_1_s = '$AMM\'A\'$ là hình chữ nhật'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Gọi $M, M'$ lần lượt là trung điểm của $BC, B'C'$. \\\\ $MM'$ là đường trung bình của hình bình hành $BCC'B'$ nên: \\\\ $\\begin{cases} MM' // BB' \\\\ MM' = BB' \\end{cases} \\Rightarrow \\begin{cases} MM' // AA' \\\\ MM' = AA' \\end{cases} \\Rightarrow AMM'A'$ là hình bình hành.''')
        
        # Đưa các lời giải vào danh sách lời giải
        list_nb_2 = [loigiai_nb_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_nb = list(zip(list_nb_1, list_nb_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_nb)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        
        ########################################################################
        # Thông hiểu 
        ########################################################################
        
        # Các đáp án
        th_da_1_d = '\\True $\\frac{AI}{AM} = \\frac{AG}{AN} = \\frac{2}{3}$'
        th_da_1_s = '$\\frac{AI}{AM} = \\frac{AG}{AN} = %s$' % (wrong_ratio)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Gọi $N$ là trung điểm của $CC'$, tam giác $AMN$ có $\\frac{AI}{AM} = \\frac{AG}{AN} = \\frac{2}{3}$ (tính chất trọng tâm). \\\\ Suy ra $IG // MN$ mà $MN \\subset (BCC'B')$ nên $IG // (BCC'B')$. (1)''')
        
        # Đưa các lời giải vào danh sách lời giải
        list_th_2 = [loigiai_th_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_th = list(zip(list_th_1, list_th_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_th)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        
        ########################################################################
        # Vận dụng 
        ########################################################################
        
        # Các đáp án
        vd_da_1_d = '\\True $(IKG) // (BCC\'B\')$'
        vd_da_1_s = '$(IKG)$ cắt $(BCC\'B\')$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Vì $I, K$ theo thứ tự là trọng tâm các tam giác $ABC, A'B'C'$ nên $IM = KM' = \\frac{1}{3}A'M' = \\frac{1}{3}AM$, mà $IM // KM'$ nên $IKM'M$ là hình bình hành. \\\\ Suy ra $IK // MM'$, mà $MM' \\subset (BCC'B') \\Rightarrow IK // (BCC'B')$. (2) \\\\ Từ (1) và (2) suy ra $(IKG) // (BCC'B')$.''')
        
        # Đưa các lời giải vào danh sách lời giải
        list_vd_2 = [loigiai_vd_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_vd = list(zip(list_vd_1, list_vd_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_vd)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        
        ########################################################################
        # Vận dụng cao 
        ########################################################################
        
        # Các đáp án
        vdc_da_1_d = '\\True $(A\'KG) // (AIB\')$'
        vdc_da_1_s = '$(A\'KG)$ cắt $(AIB\')$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Vì $(A\'KG) \\equiv (A\'M\'C)$ và $(AIB\') \\equiv (AMB\')$, ta cần chứng minh $(A\'M\'C) // (AMB\')$. \\\\ Dễ thấy $AMM\'A\'$ là hình bình hành nên $AM // A\'M\'$, mà $A\'M\' \\subset (A\'M\'C)$ nên $AM // (A\'M\'C)$. (3) \\\\ Ta có: $\\begin{cases} CM // B\'M\' \\\\ CM = B\'M\' \\end{cases} \\Rightarrow CMB\'M\'$ là hình bình hành, suy ra $B\'M // CM\'$, mà $CM\' \\subset (A\'M\'C) \\Rightarrow B\'M // (A\'M\'C)$. (4) \\\\ Từ (3) và (4) suy ra $(A\'M\'C) // (AMB\')$, hay $(A\'KG) // (AIB\')$.''')
        
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
        content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        + str(tikz_fig) + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
        
        return content