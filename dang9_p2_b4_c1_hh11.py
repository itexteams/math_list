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


def bt_dang9_p2_b4_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        # Hình vẽ TikZ chuẩn 100% theo mẫu ảnh
        tikz_fig = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (5,0);
    \\coordinate (A) at (1.5,1.5);
    \\coordinate (D) at ($(C)+(A)-(B)$);
    \\coordinate (S) at (2.5,6);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (M) at ($(S)!0.5!(A)$);
    \\coordinate (N) at ($(S)!0.5!(D)$);
    \\coordinate (P) at ($(A)!0.5!(B)$);
    \\coordinate (Q) at ($(O)!0.5!(N)$);
    \\coordinate (R) at ($(A)!0.5!(D)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S) (S)--(C);
    \\draw[line width=1pt, dashed] (B)--(A)--(D) (S)--(A) (A)--(C) (B)--(D) (M)--(N) (O)--(M) (O)--(N) (P)--(Q) (M)--(P) (P)--(O) (O)--(R) (N)--(P) (N)--(R);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (M) circle (1pt) node[above left] {$M$};
    \\fill (N) circle (1pt) node[above right] {$N$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (P) circle (1pt) node[below left] {$P$};
    \\fill (Q) circle (1pt) node[right] {$Q$};
    \\fill (R) circle (1pt) node[above right] {$R$};
\\end{tikzpicture}
\\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M, N$ lần lượt là trung điểm của $SA$ và $SD$. Khi đó:''')
        
        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '$ON // SB$'
        nb_da_1_s = '\\True $ON$ chéo nhau với $SB$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Trong tam giác $SBD$, ta có $O$ là trung điểm của $BD$ và $N$ là trung điểm của $SD$. \\\\ Do đó $ON$ là đường trung bình của tam giác $SBD$, suy ra $ON // SB$. \\\\ Do đó mệnh đề \"$ON$ chéo nhau với $SB$\" là sai.''')
        
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
        th_da_1_d = '\\True $(OMN) // (SBC)$'
        th_da_1_s = '$(OMN)$ cắt $(SBC)$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        th_da_1 = random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Ta có $OM // SC$ (do $OM$ là đường trung bình tam giác $SAC$). \\\\ Lại có $ON // SB$ (do $ON$ là đường trung bình tam giác $SBD$). \\\\ Mặt khác: $\\begin{cases} ON // SB; OM // SC \\\\ OM, ON \\subset (OMN), OM \\cap ON = O \\\\ SB, SC \\subset (SBC), SB \\cap SC = S \\end{cases} \\Rightarrow (OMN) // (SBC)$.''')
        
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
        vd_da_1_d = 'Gọi $P$ và $Q$ là trung điểm của $AB$ và $ON$. Khi đó $PQ // (SBC)$'
        vd_da_1_s = '\\True Gọi $P$ và $Q$ là trung điểm của $AB$ và $ON$. Khi đó $PQ$ cắt $(SBC)$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Gọi $P$ và $Q$ lần lượt là trung điểm của $AB$ và $ON$. \\\\ Ta có: $\\begin{cases} OP // AD (OP // BC) \\\\ MN // AD \\end{cases} \\Rightarrow OP // MN \\Rightarrow OMPN$ là hình thang $\\Rightarrow P \\in (OMN)$. \\\\ Lại có $Q \\in ON \\subset (OMN) \\Rightarrow PQ \\subset (OMN)$. \\\\ Ta có: $\\begin{cases} PQ \\subset (OMN) \\\\ (OMN) // (SBC) \\end{cases} \\Rightarrow PQ // (SBC)$. \\\\ Do đó mệnh đề \"$PQ$ cắt $(SBC)$\" là sai.''')
        
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
        vdc_da_1_d = '\\True Gọi $R$ là trung điểm $AD$. Khi đó $(MOR) // (SCD)$'
        vdc_da_1_s = 'Gọi $R$ là trung điểm $AD$. Khi đó $(MOR)$ cắt $(SCD)$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Gọi $R$ là trung điểm $AD$. \\\\ Ta có $OR // CD$ (do $OR$ là đường trung bình của tam giác $ACD$). \\\\ Lại có $OM // SC$ (do $OM$ là đường trung bình của tam giác $SAC$). \\\\ Ta có: $\\begin{cases} OM // SC \\\\ OR // CD \\\\ OM, OR \\subset (MOR), OM \\cap OR = O \\\\ SC, CD \\subset (SCD), SC \\cap CD = C \\end{cases} \\Rightarrow (MOR) // (SCD)$.''')
        
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