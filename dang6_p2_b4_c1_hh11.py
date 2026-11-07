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


def bt_dang6_p2_b4_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        # Hình vẽ TikZ chuẩn 100% theo mẫu ảnh
        tikz_fig = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (4.5,0);
    \\coordinate (A) at (1.8,1.8);
    \\coordinate (D) at ($(C)+(A)-(B)$);
    \\coordinate (S) at (2.7,5.5);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (M) at ($(S)!0.5!(A)$);
    \\coordinate (N) at ($(S)!0.5!(D)$);
    \\coordinate (E) at ($(A)!0.5!(B)$);
    \\coordinate (I) at ($(B)!0.5!(C)$);
    \\coordinate (F) at ($(O)!0.6!(N)$);
    \\coordinate (G) at ($(O)!0.4!(N)+(0.2,-0.1)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S) (S)--(C);
    \\draw[line width=1pt, dashed] (B)--(A)--(D) (S)--(A) (A)--(C) (B)--(D) (M)--(N) (M)--(E)--(F)--(O)--(M) (O)--(N) (O)--(I) (G)--(N);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (A) circle (1pt) node[above right] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (M) circle (1pt) node[above right] {$M$};
    \\fill (N) circle (1pt) node[above right] {$N$};
    \\fill (E) circle (1pt) node[below left] {$E$};
    \\fill (I) circle (1pt) node[below] {$I$};
    \\fill (F) circle (1pt) node[left] {$F$};
    \\fill (G) circle (1pt) node[right] {$G$};
\\end{tikzpicture}
\\end{center}''')
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành tâm $O$. Gọi $M, N$ lần lượt là trung điểm của $SA$ và $SD$.''')
        
        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True $MN // (SBC)$'
        nb_da_1_s = '$MN$ cắt $(SBC)$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        nb_da_1 = random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Vì $MN$ là đường trung bình của tam giác $SAD$ nên $MN // AD \\Rightarrow MN // BC \\Rightarrow MN // (SBC)$. (1)''')
        
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
        loigiai_th_1 = ('''Tương tự, ta có $O, N$ theo thứ tự là trung điểm của $BD, SD$ nên $ON$ là đường trung bình của tam giác $SBD \\Rightarrow ON // SB \\Rightarrow ON // (SBC)$. (2) \\\\ Từ (1) và (2) suy ra $(OMN) // (SBC)$.''')
        
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
        vd_da_1_d = '\\True Gọi $E$ là trung điểm đoạn $AB$ và $F$ là một điểm thuộc đoạn $ON$. Khi đó $EF // (SBC)$'
        vd_da_1_s = 'Gọi $E$ là trung điểm đoạn $AB$ và $F$ là một điểm thuộc đoạn $ON$. Khi đó $EF$ cắt với mặt phẳng $(SBC)$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        vd_da_1 = random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Ta có $OE$ là đường trung bình của tam giác $ABD$ nên $OE // AD \\Rightarrow OE // MN$. \\\\ Do đó $E \\in (OMN)$. Mặt khác $F \\in ON, ON \\subset (OMN) \\Rightarrow F \\in (OMN)$. \\\\ Ta có: $\\begin{cases} EF \\subset (OMN) \\\\ (OMN) // (SBC) \\end{cases} \\Rightarrow EF // (SBC)$.''')
        
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
        vdc_da_1_d = '\\True Gọi $G$ là một điểm trên mặt phẳng $(ABCD)$ cách đều $AB$ và $CD$. Khi đó $GN // (SAB)$'
        vdc_da_1_s = 'Gọi $G$ là một điểm trên mặt phẳng $(ABCD)$ cách đều $AB$ và $CD$. Khi đó $GN$ cắt $(SAB)$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        vdc_da_1 = random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Vì $G$ thuộc mặt phẳng $(ABCD)$ và cách đều $AB, CD$ nên $G$ thuộc đường trung bình của hình bình hành $ABCD$ (ứng với hai cạnh $AB, CD$). \\\\ Gọi $I$ là trung điểm $BC$ thì $I, O, G$ thẳng hàng. \\\\ Ta có $OI$ là đường trung bình của $\\Delta ABC$ nên $OI // AB \\Rightarrow OI // (SAB)$. (3) \\\\ Tương tự, ta có $ON // SB \\Rightarrow ON // (SAB)$. (4) \\\\ Từ (3), (4) suy ra $(OIN) // (SAB)$ mà $NG \\subset (OIN)$ nên $NG // (SAB)$.''')
        
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